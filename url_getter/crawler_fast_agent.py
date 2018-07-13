#!/usr/bin/python3

import json
import uuid
import time
import random
import requests
from multiprocessing import Queue
from configparser import ConfigParser
from requests.utils import requote_uri

import asyncio
from aiohttp import ClientSession


config = ConfigParser()
config.read('client.conf')

server_url = config.get('DEFAULT', 'server_url')
search_url = ''
TASK_ID = ''
AGENT_UUID = uuid.uuid4()

TASKS = []
TASKS_COUNT = 0
results_queue = Queue()


async def fetch(task, url, session):
    """ This method gets HTML content of pages and parses it. """

    try:
        async with session.get(url) as response:
            return task, await response.text()
    except:
        return task, ''


async def bound_fetch(sem, task, url, session):
    # Getter function with semaphore.
    async with sem:
        return await fetch(task, url, session)


async def run(search_url, tasks):
    """ This method starts the main loop of async threads. """

    async_tasks = []
    # create instance of Semaphore
    sem = asyncio.Semaphore(1000)

    # Create client session that will ensure we don't open new connection
    # per each request:
    async with ClientSession() as session:
        for task in tasks:
            # pass Semaphore and session to every GET request
            url = requote_uri(search_url.format(task))
            async_task = asyncio.ensure_future(bound_fetch(sem, task, url, session))
            async_tasks.append(async_task)

        # wait for all the results:
        return await asyncio.gather(*async_tasks, return_exceptions=False)


def init():
    """
        This method finds the server.
    """

    global server_url
    global search_url

    response = requests.get('{0}/get_search_url'.format(server_url))
    search_url = json.loads(response.text)


def get_task():
    global server_url
    global TASK_ID
    global TASKS

    # Send active status to server:
    requests.get('{0}/agents/{1}'.format(server_url, AGENT_UUID))

    response = requests.get('{0}/get_tasks_list'.format(server_url))

    all_tasks = json.loads(response.text)
    if all_tasks:
        # It is important to take the random task from the list to
        # avoid duplication of work by different crawler agents
        # (the possible duplication is not critical, but it is better
        # to avoid it):
        TASK_ID = all_tasks[random.randint(0, len(all_tasks)-1)]

        # get one random task from the list:
        response = requests.get('{0}/get_task/{1}'.format(server_url, TASK_ID))

        print("New task: {0}".format(TASK_ID))
        TASKS = json.loads(response.text)
    else:
        TASKS = []


def send_result(data):
    """ This method sends the search results to the server. """

    global server_url
    global TASK_ID

    requests.post('{0}/task_done/{1}'.format(server_url, TASK_ID), json=data,
                  headers={'Content-Type': 'application/json'})
    TASK_ID = ''


# Start the initialization of the CrawlerAgent:
init()

while True:

    try:
        get_task()
    except:
        TASK_ID = ''

    while TASK_ID != '':
        print (len(TASKS))

        start_time = int(round(time.time()))

        # Start processing of each TASK in a separate async thread:
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(run(search_url, TASKS))
        crawler_results = loop.run_until_complete(future)

        data = []
        for result in crawler_results:
            search_word, page = result
            results = []

            parsed = str(page).split('<')

            for word in parsed:
                 if word.startswith('a'):
                     if 'product' in word and 'item' in word:
                        # Get links and titles of the products from
                        # the page source:
                        href = word.split('"')[3].split('?')[0]
                        title = word.split('>')[1]

                        results.append({'title': title, 'link': href})

            # Save search request and it's results:
            data.append({'request': search_word, 'results': results})

        print('RESULTS COUNT: {0}'.format(len(data)))

        end_time = int(round(time.time()))
        print('TASK WAS DONE IN {0} SECONDS'.format(end_time - start_time))

        # Send results and get new task:
        send_result(data)
        get_task()

    time.sleep(5)
