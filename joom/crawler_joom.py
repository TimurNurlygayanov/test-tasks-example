#!/usr/bin/python3

import json
import time
from multiprocessing import Queue
from aiohttp import ClientSession
from requests.utils import requote_uri
from selenium import webdriver
from joblib import Parallel, delayed


search_url = 'https://www.joom.com/en/search/q.{0}'
results_queue = Queue()


def parse(request):
    url = requote_uri(search_url.format(request))
    browser = webdriver.PhantomJS(executable_path='./phantomjs')
    browser.get(url)

    parsed = []
    fail = False
    k = 0

    while k < 60 and (len(parsed) < 3 or fail):
        fail = False
        k += 1

        page_content = browser.page_source
        parsed = str(page_content).split('Product')
        time.sleep(0.1)

        for word in parsed:
            if word.startswith('"'):
                if len(word.split('url(')) < 2:
                    fail = True

    results = []

    for word in parsed:
        if len(results) < 20 and word.startswith('"'):
            try:

                image = word.split('url(')[1].split(')')[0]

                if (len(word.split('property="price"')) < 3):
                    price = word.split('property="price"')[1].split('>')[2].split('<')[0]
                else:
                    price = word.split('property="price"')[2].split('>')[2].split('<')[0]

                try:
                    raiting = word.split('ratingValue')[1].split('>')[2].split('<')[0]
                except:
                    raiting = 0

                href = word.split('/en/products/')[1].split('"')[0]
                href = 'https://www.joom.com/en/products/{0}'.format(href)
                title = word.split('property="name"')[1].split('>')[1].split('<')[0]

                results.append({'title': u'{0}'.format(title),
                                'position': len(results)+1,
                                'product_url': href, 'rating': raiting,
                                'price': price, 'image': image})

            except:
                # Just ignore requests which didn't find anything
                pass

    # Save search request and it's results:
    results_queue.put({'query': request, 'engine': 'joom',
                       'search_results': results})

TASKS = []

# Read stdin:
with open('requests.txt', 'r') as file_r:
    k = 0
    for search_word in file_r:
        word = search_word.replace('&quot;', '').strip()

        TASKS.append(word)

        k += 1

        if (k >= 50):

            Parallel(n_jobs=10, timeout=50000, backend='threading')\
                    (delayed(parse)(task) for task in TASKS)

            TASKS = []
            k = 0

            # Print all the results (note: it is async queue):
            while not results_queue.empty():
                result = results_queue.get()

                print(json.dumps(result, ensure_ascii=False))


time.sleep(1)

NEXT_REQUESTS = []
# Print all the results (note: it is async queue):
while not results_queue.empty():
    result = results_queue.get()
    print(json.dumps(result, ensure_ascii=False))

with open('requests_next.txt', 'w') as file_r:
    for r in NEXT_REQUESTS:
        file_r.write(r + '\n')
