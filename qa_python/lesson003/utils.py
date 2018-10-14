#!/usr/bin/python3
# -*- encoding=utf8 -*-

import requests
from requests.auth import HTTPBasicAuth
from configparser import ConfigParser
from uuid import UUID

config = ConfigParser()
config.read('test_config.conf')


def get_conf_param(section, parameter, default_value):
    result = config.get(section, parameter)
    return result or default_value


# Read all parameters from config file:
user = get_conf_param('DEFAULT', 'user', '')
password = get_conf_param('DEFAULT', 'password', '')
host = get_conf_param('DEFAULT', 'host', 'http://0.0.0.0:7000')


def validate_uuid4(uuid_string):
    """ This function allows to check UUID. """

    try:
        val = UUID(uuid_string, version=4)
    except ValueError:
        return False

    return val.hex == uuid_string.replace('-', '')


def get(url, cookies=None, auth_data=None):
    """ This function sends REST API GET request and prints some
        useful information for debugging.
    """

    result = requests.get(url, cookies=cookies, auth=auth_data)

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


def put(url, cookies=None, body=None):
    """ This function sends REST API PUT request and prints some
        useful information for debugging.
    """

    result = requests.put(url, cookies=cookies, data=body)

    print('PUT request to {0}'.format(url))
    print('Status code: {0}'.format(result.status_code))
    print('RESPONSE: {0}'.format(result.text))

    return result


def delete(url, cookies=None):
    """ This function sends REST API DELETE request and prints some
        useful information for debugging.
    """

    result = requests.delete(url, cookies=cookies)

    print('DELETE request to {0}'.format(url))
    print('Status code: {0}'.format(result.status_code))
    print('RESPONSE: {0}'.format(result.text))

    return result


def auth():
    """ This function allows to get auth cookie. """

    url = '{0}/login'.format(host)
    auth_data = HTTPBasicAuth(user, password)

    response = get(url, auth_data=auth_data)
    data = response.json()

    # Return auth_cookie:
    return {'my_cookie': data['auth_cookie']}


def get_all_books():
    """ This function returns full list of books. """

    url = '{0}/books'.format(host)
    response = get(url, cookies=auth())

    return response.json()


def get_book(book_id='1'):
    """ This function returns one book. """

    url = '{0}/books/{1}'.format(host, book_id)
    response = get(url, cookies=auth())

    return response.json()


def add_book(book):
    """ This function creates new book. """

    url = '{0}/add_book'.format(host)
    response = post(url, cookies=auth(), body=book)

    return response.json()


def delete_book(book_id='1'):
    """ This function deletes the book. """

    url = '{0}/books/{1}'.format(host, book_id)
    delete(url, cookies=auth())


def update_book(book_id, book):
    """ This function updates information about the book. """

    url = '{0}/books/{1}'.format(host, book_id)
    response = put(url, cookies=auth(), body=book)

    return response.json()
