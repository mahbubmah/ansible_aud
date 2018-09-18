from flask import Flask, render_template
import os
from utility import read_anisble_log

app = Flask(__name__)
#app.debug = True
#app.run(host='0.0.0.0')

@app.route("/")
def hello():
	
	res_data={}
	res_data['LastRunTime']='Test LastRunTime string'
	res_data['log']=read_anisble_log('log.txt')

	return render_template('ansible_log.html', data=res_data)

if __name__ == "__main__":
	app.run()
	# app.run(host='0.0.0.0')
