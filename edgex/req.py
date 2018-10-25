# importing the requests library
import requests
from time import sleep
def get(url, params = {}):
    r = requests.get(url=url, params=params)
    return r.status_code, r.json

def post(url, params):
    print('-------')
    print("posting " + str(params).replace('\'','\"'))
    r = requests.post(url=url, data = str(params).replace('\'','\"'))
    return r.status_code, r.text


def filepost(url, params):
    print('-------')
    print("posting " + str(params).replace('\'','\"'))
    r = requests.post(url=url, files = params)
    return r.status_code, r.text

#specific to edgex
#{'serverdata': <phonenumber>}
def put(device, params):
    code, json = get('http://localhost:48082/api/v1/device/name/' + device)
    url = json["put"]["url"]
    print('-------')
    print("putting " + str(params).replace('\'', '\"'))
    r = requests.put(url=url, data = str(params).replace('\'','\"'))
    return r.status_code, r.content

