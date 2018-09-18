def findClass(ip_addr):
	ip=int(ip_addr[:ip_addr.find('.')])
	if ip >=1 and ip <= 126:
		return 'A'
	elif ip >= 128 and ip <= 191:
		return 'B'
	elif ip >= 192 and ip <= 223:
		return 'C'
	elif ip >= 224 and ip <= 239:
		return 'D' 
	else:
		return 'E'

def read_anisble_log(log_path):
	result=[]
	with open(log_path,'r') as fs:
		for line in fs.readlines():
			if line.find('inet ')>0 and line.find('scope global')>0:
				ip=line[line.find('inet ')+5:line.find('/')]				
				ip_class = findClass(ip)
				result.append([ip,ip_class])
				# print("IP address "+ip+" belongs to Class "+ip_class)
	ret_data=[]
	for i in result:
		log={}		
		log['time']='test time'
		log['ip']=i[0]
		log['class']=i[1]
		log['msg']="IP address "+i[0]+" belongs to Class "+i[1]
		ret_data.append(log)
	return ret_data

if __name__ == "__main__":
	# s_ip = "130.45.151.154"
	# # print(s_ip[10])
	# ipClass = findClass(s_ip)
	# print("Given IP address belongs to Class "+ipClass)


	log_path='*log.txt'    
	data=read_anisble_log(log_path)
	# print	(data)
