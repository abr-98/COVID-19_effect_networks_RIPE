import os
import subprocess
import re
import ipaddress
import json

def runProcess(exe):    
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while(True):
        # returns None while subprocess is running
        retcode = p.poll() 
        line = p.stdout.readline()
        yield line
        if retcode is not None:
            break


def list_ip(IP):

	file=IP+'_details.json'
	l=[]
	ip_list={}
	for line in runProcess('curl https://api.hackertarget.com/aslookup/?q=AS15169'.split()):
		if re.match("[0-9]+.[0-9]+.[0-9]+.[0-9]+",line.decode('utf-8')[:-1]):
			l.append(line.decode('utf-8')[:-1])
	print(len(l))
	print(l)
	all_ips=[]
	#temp_ip=[]
	k=1
	for i in  l:
		k+=1
		#if k==len(i)-3:
		#	continue
		temp_ip=[str(ip) for ip in ipaddress.IPv4Network(i)]
		all_ips.append(temp_ip)
	print(len(all_ips))
	for i in all_ips:
		for j in i:
			if ip_list.get(j) is None:
				ip_list[j]=0

	with open(file,'w') as fp:
		json.dump(ip_list, fp)
#print(len(all_ips[0]))

list_ip('15169')