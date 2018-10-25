import setup

#name = 'test' + str(random.randint(0, 100))
#name = 'test-get-put'

def provision_device(device_name, server, device_ip, device_port, device_service_port):
    print('Setting addressable----------')
    print(setup.provision_device_addressable(device_name, server, device_ip, device_port, device_service_port))
    print('Setting device service-------')
    print(setup.create_device_service(device_name, server, device_name + ' device service', device_name))
    print('Provisioning device----------')
    print(setup.provision_device(device_name, server, device_name, device_name, device_name, 'testprofile'))

#specific to our application
def provision_data(server):
    print('Setting value descriptors----')
    print(setup.value_descriptor('location', server, 'data from device', 'S', 'none'))
    print(setup.value_descriptor('phone', server, 'data from device', 'S', 'none'))
    print(setup.value_descriptor('serverdata', server, 'data from device', 'S', 'none'))
    print('Setting device profile-------')
    print(setup.create_device_profile(server, 'test.yml'))
