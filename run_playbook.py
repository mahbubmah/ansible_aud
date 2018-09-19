import subprocess
import sys
import os
import io
import datetime



def run_ansible_playbook(playbook_name):
	# return 'playbook '+playbook_name+' run successfully'
	subprocess.call(shlex.split('chmod +x test_cmd.sh'))	
	cmd="ansible-playbook "+playbook_name
	pipe = subprocess.Popen(["ansible-playbook",playbook_name], stdout=subprocess.PIPE, bufsize=10**8)

	pipe.wait()

	output= pipe.stdout.read()
	with open('log'+os.sep+os.path.splitext(playbook_name)[0]+'_log_'+datetime.datetime.now().strftime("%Y%m%d_%H%M%S")+'.txt','w+') as f:
		f.write(output)

	return 'playbook '+playbook_name+' run successfully'



if __name__ == "__main__":
    playbook_name=sys.argv[1]
    print(run_ansible_playbook(playbook_name))
        

