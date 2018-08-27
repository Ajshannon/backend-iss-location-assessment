import requests
import json


api_url_base = 'http://api.open-notify.org/astros.json'
headers = {'Content-Type': 'application/json'}


def astro():
    api = api_url_base

    response = requests.get(api, headers=headers)

    if response.status_code == 200:
        repositories = json.loads(response.content.decode('utf-8'))

        people = repositories['people']

        print "people in space: " + str(repositories['number'])
        for person in people:
            print person['name'] + " " + person['craft']

    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api))
        return None
