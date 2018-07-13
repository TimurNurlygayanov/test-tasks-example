#!/usr/bin/python3

import os
import uuid
import json
import time
import shutil
import glob
from demjson import decode
from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from flask import send_from_directory
from configparser import ConfigParser
from werkzeug.utils import secure_filename


TASKS = []
TASKS_COUNT = 0
ACTIVE_AGENTS = {}
SENT_RESULTS = []
START_TIME = int(round(time.time()))

app = Flask(__name__, static_folder='./')
app.config['UPLOAD_FOLDER'] = '/var/tmp/'
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024

config = ConfigParser()
config.read('server.conf')


def get_conf_param(section, parameter, default_value):
    result = config.get(section, parameter)
    return result or default_value


@app.route('/get_tasks_list', methods=['GET'])
def tasks_list():
    """
        This method returns the list of tasks.
    """

    global TASKS
    return jsonify(TASKS)


@app.route('/get_search_url', methods=['GET'])
def get_search_url():
    """
        This method returns the URL for search.
    """

    global SEARCH_URL

    return jsonify(SEARCH_URL)


@app.route('/get_task/<task_id>', methods=['GET'])
def get_task(task_id):
    """
        This method returns the list of search requests for Crawler Agents.
    """

    global REQUESTS_FILE
    global TASKS_PER_AGENT

    tasks = []

    with open(REQUESTS_FILE, 'r') as search_requests:
        search_requests.seek(int(task_id))

        # read TASKS_PER_AGENT lines from file:
        for line in search_requests:
            tasks.append(u'{0}'.format(line.rstrip()))

            if len(tasks) >= TASKS_PER_AGENT:
                break

    return jsonify(tasks)


@app.route('/get_stream_results_json', methods=['GET'])
def get_stream_results():
    global SENT_RESULTS

    files = glob.glob("results/*.txt")

    for file in files:
        if file not in SENT_RESULTS and os.path.getsize(file):
            SENT_RESULTS.append(file)

            return send_from_directory(directory='./results',
                                       filename=file.split('/')[-1])

    return jsonify([])


@app.route('/agents/<agent_id>', methods=['GET'])
def get_agent(agent_id):
    """
        This method saves information about active Crawler Agents.
    """

    global ACTIVE_AGENTS

    timestamp = int(round(time.time()))
    ACTIVE_AGENTS[agent_id] = timestamp

    return jsonify(timestamp)


@app.route('/task_done/<task_id>', methods=['POST'])
def save_results(task_id):
    """
        This method collects results from Agents and save all results to
        the separate files.
    """

    global TASKS

    task_id = int(task_id)

    if task_id in TASKS:
        TASKS.remove(task_id)

        if not os.path.isfile('results/{0}.txt'.format(task_id)):
            with open('results/{0}.txt'.format(task_id), 'w') as results_file:
                data = str(request.get_json(force=True))
                results_file.write('{0}'.format(data))

    return 'Thank you!'


@app.route('/detailed_progress', methods=['GET'])
def detailed_progress():
    global TASKS
    global TASKS_COUNT
    global ACTIVE_AGENTS
    global START_TIME
    global TASKS_PER_AGENT

    time_now = int(round(time.time()))
    work_time = time_now - START_TIME or 1

    performance = (TASKS_COUNT - len(TASKS)) / work_time

    time_to_finish = int(round(len(TASKS) / (60*performance)
                               if performance else 0))

    performance = int(round(performance * TASKS_PER_AGENT))

    # Get the current progress:
    progress = len(TASKS)

    agents_count = 0

    time_now = int(round(time.time()))
    for agent in ACTIVE_AGENTS:
        if time_now - ACTIVE_AGENTS[agent] < 60:
            agents_count += 1

    return render_template('detailed_progress.html', progress=progress,
                           total=TASKS_COUNT, agents_count=agents_count,
                           performance=performance,
                           time_to_finish=time_to_finish)


@app.route('/', methods=['GET'])
def human_progress():
    global TASKS
    global TASKS_COUNT
    global ACTIVE_AGENTS
    global START_TIME
    global TASKS_PER_AGENT

    time_now = int(round(time.time()))
    work_time = time_now - START_TIME or 1

    performance = (TASKS_COUNT - len(TASKS)) / work_time

    time_to_finish = int(round(len(TASKS) / (60*performance)
                               if performance else 0))

    performance = int(round(performance * TASKS_PER_AGENT))

    # Get the current progress:
    progress = len(TASKS)

    agents_count = 0

    time_now = int(round(time.time()))
    for agent in ACTIVE_AGENTS:
        # Active agent should take task at least each 10 minutes:
        if time_now - ACTIVE_AGENTS[agent] < 10 * 60:
            agents_count += 1

    return render_template('new_task.html', progress=progress,
                           total=TASKS_COUNT, agents_count=agents_count,
                           performance=performance,
                           time_to_finish=time_to_finish)


@app.route('/crawler_results', methods=['GET'])
def download():
    shutil.make_archive('results', 'zip', 'results')
    return send_from_directory(directory='./', filename='results.zip')


@app.route('/', methods=['POST'])
def run_crawlers():
    global TASKS
    global TASKS_PER_AGENT
    global TASKS_COUNT
    global REQUESTS_FILE
    global START_TIME
    global SENT_RESULTS

    file = request.files.get('file')

    if file:
        filename = secure_filename(str(uuid.uuid4()) + file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        REQUESTS_FILE = file_path
        TASKS = []

        with open(file_path, 'r') as search_requests:
            i = 1

            TASKS.append(search_requests.tell())
            line = search_requests.readline()
            while line:

                if i % TASKS_PER_AGENT == 0:
                    # save position of the reader each TASKS_PER_AGENT lines:
                    TASKS.append(search_requests.tell())

                line = search_requests.readline()
                i += 1

    TASKS_COUNT = len(TASKS)
    SENT_RESULTS = []
    START_TIME = int(round(time.time()))

    # Remove old results:
    files = glob.glob('results/*.txt')
    for f in files:
        os.remove(f)

    return render_template('new_task.html', progress=1,
                           total=100, agents_count=1)


# Read parameters and prepare the list of tasks:

SEARCH_URL = get_conf_param('DEFAULT', 'search_url', 'google.com')
TASKS_PER_AGENT = int(get_conf_param('DEFAULT', 'tasks_per_agent', 200))
REQUESTS_FILE = get_conf_param('DEFAULT', 'requests_file',
                               'search_requests.txt')


TASKS_COUNT = len(TASKS)

app.run('0.0.0.0')
