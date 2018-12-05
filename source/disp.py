import device_setup as setup
import random

#name = 'test' + str(random.randint(0, 100))
name = 'road-display'
server = '10.0.0.52'
client = '10.0.0.67'
print(setup.provision_device_addressable(name, server, client, 5000, 5555))
print(setup.value_descriptor('data', server, 'data from device', 'S', 'none'))
print(setup.create_device_profile(server, 'disp.yml'))
print(setup.create_device_service(name, server, name + ' device service', name))
print(setup.provision_device(name, server, name, name, name, 'roadprofile'))

