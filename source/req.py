# importing the requests library
import requests
import json
from time import sleep
def get(url, params = {}):
    r = requests.get(url=url, params=params)
    print('got----')
    print(r.text)
    return r.status_code, json.loads(r.text)

def post(url, params):
    print('-------')
    print("posting " + str(params).replace('\'','\"'))
    r = requests.post(url=url, data = str(params).replace('\'','\"'))
    print(r.status_code, r.text)
    return r.status_code, r.text


def filepost(url, params):
    print('-------')
    print("posting " + str(params).replace('\'','\"'))
    r = requests.post(url=url, files = params)
    print(r.status_code, r.text)
    return r.status_code, r.text

#specific to edgex
#{'serverdata': <phonenumber>}
def put(device, params, server):
    code, json = get('http://localhost:48082/api/v1/device/name/' + device)
    url = json["commands"][0]["put"]["url"]
    arr = url.split('/')
    random, port = arr[2].split(':')
    arr[2] = server + ':' + port
    url = '/'.join(arr)
    print('-------')
    print("putting " + str(params).replace('\'', '\"') + ' to ' + url)
    r = requests.put(url=url, data = str(params).replace('\'','\"'))
    print(r.status_code, r.content)
    return r.status_code, r.content

