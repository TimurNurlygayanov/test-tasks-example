#!/usr/bin/python3
# -*- encoding=utf8 -*-

import requests


def check_ip(ip):
    numbers = ip.split('.')
    numbers = [int(k) for k in numbers]

    for i in numbers:
        if i < 0 or i > 255:
            return False

    return True


def test_check_country():
    result = requests.get('http://ip-api.com/json')
    data = result.json()

    country = data.get('country')

    assert country == 'Cyprus', 'Country is wrong!'


def test_check_ip():
    result = requests.get('http://ip-api.com/json')
    data = result.json()

    ip = data.get('query')

    assert len(ip) > 0
    assert ip > ''
    assert check_ip(ip)
