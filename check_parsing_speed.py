import requests
import time
from joblib import Parallel, delayed
from multiprocessing import Queue


results_queue = Queue()


data = requests.get('http://tmall.aliexpress.com/wholesale?q=tv')
text = data.text

print(text)

all_data = [text for i in range(100000)]

results = []

"""
start_time = int(round(time.time()))

for t in all_data:
    items = t.split('/item')

    for item in items:
        if item.startswith('/'):
            p_id = item.split('.html')[0].split('/')[-1]
            results.append(p_id)


end_time = int(round(time.time()))
print('1 thread TASK WAS DONE IN {0} SECONDS'.format(end_time - start_time))
print('Results: ', len(results))
print('\n\n\n')
"""


def check(t):

    items = t.split('/item')

    for item in items:
        if item.startswith('/'):
            p_id = item.split('.html')[0].split('/')[-1]
            results_queue.put(p_id)


def check2(t):

    items = t.split('/item')

    for item in items:
        if item.startswith('/'):
           p_id = item.split('.html')[0].split('/')[-1]
           results.append(p_id)


results = []
start_time = int(round(time.time()))

# Run function "check" in 10 threads:
#, backend='threading') \
Parallel(n_jobs=10, timeout=300) \
        (delayed(check)(task) for task in all_data)

end_time = int(round(time.time()))
print('10 threads TASK WAS DONE IN {0} SECONDS'.format(end_time - start_time))
print('Results: ', results_queue.qsize())
print('\n\n\n')

start_time = int(round(time.time()))

# Run function "check" in 10 threads:
#, backend='threading') \
Parallel(n_jobs=100, timeout=300) \
        (delayed(check2)(task) for task in all_data)

end_time = int(round(time.time()))
print('10 threads TASK WAS DONE IN {0} SECONDS'.format(end_time - start_time))
print('Results: ', len(results))
