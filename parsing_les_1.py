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
        # pprint(data)
        # print(type(data))
    print(repos)
