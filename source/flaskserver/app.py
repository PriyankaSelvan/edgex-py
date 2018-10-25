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
	return 'Success'

if __name__ =='__main__':
	app.run(debug=True)
