import requests
import json


def check_ip(ip):
    numbers = ip.split('.')

    for n in numbers:
        if int(n) <= 0 or int(n) > 255:
            return False

    return True


def test_simple01():
    result = requests.get('http://ip-api.com/json')
    data = json.loads(result.text)

    assert data['city'] == 'St Petersburg'


def test_simple02():
    result = requests.get('http://ip-api.com/json')

    assert result.status_code == 200


def test_check_ip():
    result = requests.get('http://ip-api.com/json')
    data = json.loads(result.text)

    ip = data['query']

    assert check_ip(ip)
