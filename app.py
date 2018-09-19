from flask import *
import os
from utility import *
from run_playbook import *

app = Flask(__name__)

@app.route("/")
def index():	
	first_cmd_run_time_str,data=get_ip_info_from_log('./log')
	res_data={}
	res_data['FirstRunTime']=first_cmd_run_time_str
	res_data['log']=data
	res_data['pb_list']=get_playbook_list('./playbook')

	# if session.get('msg') == True:
	# 	res_data['sess_msg']=session['msg']
	# else:
	# 	res_data['sess_msg']

	# session['msg']=''

	return render_template('ansible_log.html', data=res_data)

@app.route("/run_playbook", methods=['POST'])
def run_playbook():
	play_book_name=request.form['play_book_name']	
	session['msg']=run_ansible_playbook(play_book_name)
	return redirect(url_for('index'))

if __name__ == "__main__":
	app.secret_key = 'super secret key'
	app.run(host='0.0.0.0')
