#!/usr/bin/python3
# -*- encoding=utf8 -*-

import requests

from config import host


def get(url, cookies=None):
    """ This function sends REST API GET request and prints some
        useful information for debugging.
    """

    result = requests.get(url, cookies=cookies)

    print('GET request to {0}'.format(url))
    print('Status code: {0}'.format(result.status_code))
    print('RESPONSE: {0}'.format(result.text))

    return result


def post(url, cookies=None, body=None):
    """ This function sends REST API POST request and prints some
        useful information for debugging.
    """

    result = requests.post(url, cookies=cookies, data=body)

    print('POST request to {0}'.format(url))
    print('Status code: {0}'.format(result.status_code))
    print('RESPONSE: {0}'.format(result.text))

    return result


def get_all_books():
    """ This function returns full list of books. """


print(host)
