from flask import json
from flask import request
from flask import Flask
from namegenerator import generate_word
import provision
import lookup
import req

app = Flask(__name__)

@app.route('/query', methods = ['POST'])
def api_message():
	#priyas device
	device_name = generate_word(4)
	print (request.get_json())
	print (device_name)
	#start of device stuff
	server = 'localhost'
	ip = request.remote_addr
	port1 = 4996
	port2 = 4997
	location = request.get_json()['location']

	#provisioning device
	provision.provision_device(device_name, server, ip, port1, port2)

	#do lookup for phone number
	phone_num = lookup.get_phone(server, location)

	#put to edgex
	req.put(device_name, {'serverdata':phone_num}, server)
	req.put('road-display', {'data':''}, 'localhost')
	#end of device stuff
	#return ('Success')
	return {'serverdata':phone_num}

if __name__ =='__main__':
	provision.provision_data('localhost')
	app.run(debug=True, host='0.0.0.0', port=4996)
