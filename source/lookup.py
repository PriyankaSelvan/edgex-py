import event

def get_phone(server, location):
    code, json1 = event.get_reading(server, 'location', 10)
    code, json2 = event.get_reading(server, 'phone', 10)
    created = ""
    print(json1)
    for field in json1:
        if field["value"] == location:
            created = field["created"]
            break

    if created:
        for field in json2:
            if field["created"] == created:
                return field["value"]
    else:
        return "notindb"
