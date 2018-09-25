import requests
import json


result = requests.get('http://ip-api.com/json')

# print(result.text)
# print(result.status_code)

data = json.loads(result.text)

print('Response status code:', result.status_code)
print('Country:', data['country'])
print('IP:', data['query'])

ip = data['query']
print('IP numbers:', ip.split('.'))
