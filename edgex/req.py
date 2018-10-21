# importing the requests library
import requests
from time import sleep
def get(url, params = {}):
    r = requests.get(url=url, params=params)
    return r.status_code, r.json

def post(url, params):
    sleep(2)
    print('-------')
    print("posting " + str(params).replace('\'','\"'))
    r = requests.post(url=url, data = str(params).replace('\'','\"'))
    return r.status_code, r.text


def filepost(url, params):
    print('-------')
    print("posting " + str(params).replace('\'','\"'))
    r = requests.post(url=url, files = params)
    return r.status_code, r.text

def put(url, params):
    r = requests.put(url=url, json = params)
    return r.status_code, r.content

