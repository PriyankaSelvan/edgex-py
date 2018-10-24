import req

#readings is a list of dicts with 2 keys. name and value
def send_reading(server, device, readings):
    req.post('http://localhost:48080/api/v1/event', {"device":device, "readings":readings})

def get_reading(server, device):
    code, json = req.get('http://localhost:48080/api/v1/event/device/' + device)
