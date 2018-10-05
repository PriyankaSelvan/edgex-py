# importing the requests library
import requests

def get(url, params = {}):
    r = requests.get(url=url, params=params)
    return r.status_code, r.json

def post(url, params):
    r = requests.post(url=url, json = params)
    return r.status_code, r.text

def put(url, params):
    r = requests.put(url=url, json = params)
    return r.status_code, r.content

