import event
data = [('12345', '7203452928'), ('09876', '7203452323')]

for tup in data:
    readings = [{"name": "location", "value": tup[0]}, {"name": "phone", "value": tup[1]}]
    event.send_reading('localhost', 'test-dummy', readings)
