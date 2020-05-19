import pandas as pd
import os
import ipaddress
import json

file_1='youtube.csv'
file_2='youtube.json'

df=pd.read_csv(file_1)
i=0
all_ips=[]
l=[]
while i<len(df):
	l.append(df.iloc[i]['ip'])
	i+=1
print(l)
ip_list={}
for i in  l:
		#k+=1
		#if k==len(i)-3:
		#	continue
		temp_ip=[str(ip) for ip in ipaddress.IPv4Network(i)]
		all_ips.append(temp_ip)
print(len(all_ips))
for i in all_ips:
		for j in i:
			if ip_list.get(j) is None:
				ip_list[j]=0

with open(file_2,'w') as fp:
	json.dump(ip_list, fp)


