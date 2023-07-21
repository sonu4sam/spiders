import requests

session = requests.Session()

# may pass in some custome cookies
r = session.get('http://httpbin.org/get', cookies={'my-cookie': 'browser'})
print(r.text)

r = requests.get('http://httpbin.org/stream/20', stream=True)

import json

for line in r.iter_lines():
    # filter out keep-alive new lines
    if line:
        decoded_line = line.decode('utf-8')
        print(json.loads(decoded_line))