import requests
from requests.auth import HTTPBasicAuth


user = 'test_user'
password = 'test_password'


def test_check_login():
    url = 'http://localhost:7000/login'
    result = requests.get(url, auth=HTTPBasicAuth(user, password))
    assert result.status_code == 200
