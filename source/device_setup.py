import req
def addressable(name, server, deviceip, deviceport, device_endpoint,
                publisher = 'none', username = 'none', password = 'none',topic = 'none'):
    url = 'http://' + server + ':48081/api/v1/addressable'
    body = {'name':name,
            'protocol': 'HTTP',
            'address': deviceip,
            'port':deviceport,
            'path': device_endpoint,
            'publisher':publisher,
            'user': username,
            'password': password,
            'topic': topic}
    return req.post(url, body)

def value_descriptor(name, server, description, type, unit, default='', formatting='%s', mini='', maxi=''):
    url = 'http://' + server + ':48080/api/v1/valuedescriptor'
    body = {'name':name,
            'description':description,
            'min':mini,
            'max':maxi,
            'type':type,
            'uomLabel':unit,
            'defaultValue':default,
            'formatting':formatting,
            'labels': [name]
            }
    return req.post(url, body)

def generate_device_profile():
    return 'notimplemented'
    #TODO Future work


def create_device_profile(server, filepath):
    url = 'http://' + server + ':48081/api/v1/deviceprofile/uploadfile'
    body = {'file': open(filepath).read()}
    return req.filepost(url, body)

def create_device_service(name, server, description, addressable_name, adminState='unlocked', operatingState='enabled'):
    url = 'http://' + server + ':48081/api/v1/deviceservice'
    body = {'name':name,
            'description':description,
            'labels': [name],
            'adminState':adminState,
            'operatingState':operatingState,
            'addressable': {'name':addressable_name}}
    return req.post(url, body)

def provision_device(name, server, description, addressablename, servicename, profilename, adminState='unlocked', operatingState='enabled'):
    url = 'http://' + server + ':48081/api/v1/device'
    body = {'name':name,
            'description':description,
            'adminState':adminState,
            'operatingState':operatingState,
            'addressable':{'name':addressablename},
            'labels':[name],
            'service':{'name':servicename},
            'profile':{'name':profilename}}
    return req.post(url, body)

def provision_device_addressable(name, server, deviceip, deviceport, serviceport):
    addressable(name, server, deviceip, deviceport, '/'+name)
    addressable(name+'control', server, deviceip, deviceport, '/'+name+'control')












