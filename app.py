from flask import Flask, render_template
import os
from utility import *

app = Flask(__name__)
#app.debug = True
#app.run(host='0.0.0.0')

@app.route("/")
def hello():
	
	last_cmd_run_time_str,data=get_ip_info_from_log('./log')
	res_data={}
	res_data['LastRunTime']=last_cmd_run_time_str
	res_data['log']=data

	return render_template('ansible_log.html', data=res_data)

if __name__ == "__main__":
	app.run()
	# app.run(host='0.0.0.0')
