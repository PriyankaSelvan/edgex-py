import setup
import random

name = 'test' + str(random.randint(0, 100))
print(setup.provision_device_addressable(name, 'localhost', '2.2.2.2', '4444', '5555'))
print(setup.value_descriptor('devicedata', 'localhost', 'data from device', 'S', 'none'))
print(setup.value_descriptor('serverdata', 'localhost', 'data from device', 'S', 'none'))
print(setup.create_device_profile('localhost', 'test.yml'))
print(setup.create_device_service(name, 'localhost', name + ' device service', name))
print(setup.provision_device(name, 'localhost', name, name, name, 'testprofile'))

