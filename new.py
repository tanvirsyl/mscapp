import json
import requests
response=requests.get('https://api.stackexchange.com/2.3/questionsorder=desc&sort=activity&site=stackoverflow')
print(response.json()['items'])