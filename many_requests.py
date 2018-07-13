#!/usr/bin/python3

from requests.utils import requote_uri
import time

import asyncio
from aiohttp import ClientSession



async def fetch(url, session):
    """ This method gets HTML content of pages. """

    try:
        async with session.get(url) as response:
            return await response.text()
    except:
        return ''   # just send an empty data in case of any errors


async def bound_fetch(sem, url, session):
    # Getter function with semaphore.
    async with sem:
        return await fetch(url, session)


async def run(urls):
    """ This method starts the main loop of async threads. """

    async_tasks = []
    # Create instance of Semaphore
    sem = asyncio.Semaphore(10000)

    # Create client session that will ensure we don't open new connection
    # per each request:
    async with ClientSession() as session:
        for url in urls:
            # pass Semaphore and session to every GET request
            url = requote_uri(url)
            async_task = asyncio.ensure_future(bound_fetch(sem, url, session))
            async_tasks.append(async_task)

        # wait for all the results:
        return await asyncio.gather(*async_tasks, return_exceptions=False)


start_time = int(round(time.time()))

urls = ['http://mail.ru' for i in range(100)]
# Start processing of each url in a separate async thread:
loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(urls))
crawler_results = loop.run_until_complete(future)


end_time = int(round(time.time()))
print('2 TASK WAS DONE IN {0} SECONDS'.format(end_time - start_time))


print('Results:', len(crawler_results))


