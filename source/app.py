from flask import json
from flask import request
from flask import Flask
from namegenerator import generate_word
import edgex

app = Flask(__name__)

@app.route('/query', methods = ['POST'])
def api_message():
	device_name = generate_word(10)
	print (request.get_json())
	print (device_name)
	#start of device stuff
	server = 'localhost'
	ip = request.remote_addr
	port1 = '4996'
	port2 = '4997'
	location = request.get_json()['location']

	#provisioning device
	edgex.provision.provision_device(device_name, server, ip, port1, port2)

	#do lookup for phone number
	phone_num = edgex.lookup.get_phone(server, location)

	#put to edgex
	edgex.req.put(device_name, {'serverdata':phone_num})

	#end of device stuff
	return 'Success'

if __name__ =='__main__':
	edgex.provision.provision_data('localhost')
	app.run(debug=True)
