import requests
import json

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

main_link = "https://api.github.com/users/agamora/repos"

response = requests.get(main_link)

if response.ok:
    if response.ok:

        data = json.loads(response.text)
    repos = []
    for i in data:
        repos.append(i['name'])
    print(repos)


from pprint import pprint
import requests
import json
import time
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

main_link = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json & ' \
            'AIzaSyB7SNmXXbNEe81dmQ77_bbRa1e0lsKL-c0parameters & London'


response = requests.get(main_link)

if response.ok:
    time.sleep(1)
    data = json.loads(response.text)
    pprint(data)
