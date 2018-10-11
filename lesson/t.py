import requests


result = requests.get('http://ip-api.com/json')

data = result.json()

print(data.get('country'))
print(data.get('query'))

print(data.get('test', 'NOT FOUND'))

