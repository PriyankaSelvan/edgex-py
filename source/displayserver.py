from flask import request
from flask import render_template
from flask import Flask


app = Flask(__name__)
flag = 0
@app.route('/disp')
def show():
        global flag
	if flag == 0 :
		return render_template('green.html')
	else :
		return render_template('red.html')

@app.route('/flip', methods=['PUT'])
def flip():
        global flag
	if flag ==0:
		flag = 1
	else:
		flag = 0
	return 'Success'
