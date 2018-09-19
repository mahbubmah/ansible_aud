import glob as gb
import os
import datetime as dt

def findClass(ip_addr):
	ip=int(ip_addr[:ip_addr.find('.')])
	if ip >=1 and ip <= 126:
		return ('A','green')
	elif ip >= 128 and ip <= 191:
		return ('B','blue')
	elif ip >= 192 and ip <= 223:
		return ('C','red')
	elif ip >= 224 and ip <= 239:
		return ('D' ,'black')
	else:
		return ('E','white')

def read_anisble_log(log_path):
	result=[]
	with open(log_path,'r') as fs:
		for line in fs.readlines():
			if line.find('inet ')>0 and line.find('scope global')>0:
				ip=line[line.find('inet ')+5:line.find('/')]				
				ip_class = findClass(ip)
				result.append([ip,ip_class])
				# print("IP address "+ip+" belongs to Class "+ip_class)
	return result;

def get_ip_info_from_log(log_dir):
	ret_data=[]

	lf_list=gb.glob(log_dir+os.sep+'*_log_*.txt')
	lf_list.sort(key=lambda x:os.path.getmtime(x),reverse=True)

	first_cmd_run_time_str=''
	for log_path in lf_list:
		log_file_name=os.path.splitext(os.path.basename(log_path))[0]
		lm_under_char_pos=[pos for pos, char in enumerate(log_file_name) if char=='_']
		lm_time_str=log_file_name[lm_under_char_pos[-2]+1:lm_under_char_pos[-2]+16]
		lm_time=dt.datetime.strptime(lm_time_str,"%Y%m%d_%H%M%S")

		first_cmd_run_time_str=lm_time.strftime("%a %b %d %H:%M:%S %Z %Y")

		log_result=read_anisble_log(log_path)
		
		for i in log_result:
			log={}
			log['time']=lm_time.strftime("%b %d, %Y %H:%M:%S") #impletemnt correct time string format
			log['ip']=i[0]
			log['class']=i[1][0]
			log['class_color']=i[1][1]
			log['msg']="IP address "+i[0]+" belongs to Class "+i[1][0]
			ret_data.append(log)
	
	return (first_cmd_run_time_str,ret_data)

def get_playbook_list(playbook_path):
	pb_list=gb.glob(playbook_path+os.sep+'*.yml')
	pb_list.sort(key=lambda x:x)

	ret_pb_list=[]
	for pb in pb_list:
		pb_item=[os.path.splitext(os.path.basename(pb))[0],os.path.basename(pb)]
		ret_pb_list.append(pb_item)

	return ret_pb_list


if __name__ == "__main__":
	# s_ip = "130.45.151.154"
	# # print(s_ip[10])
	# ipClass = findClass(s_ip)
	# print("Given IP address belongs to Class "+ipClass)
	print(get_playbook_list('./playbook'))

	# log_path='./log'    
	# data=get_ip_info_from_log(log_path)
	# print(data)
