import event

def get_phone(server, device, location):
    code, json = event.get_reading(server, device)
    for field in json:
        if field["readings"][0]["value"] == location:
            return field["readings"][1]["value"]
    return 'nophoneindb'