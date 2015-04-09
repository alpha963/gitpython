# -*- coding: utf-8 -*-
#coding=utf-8
import datetime
import paramiko

def openinfo(filenam):
	infoip= open(filenam)  
	try:
		text = infoip.read( )  
	finally:
		infoip.close( ) 
	str1=text.split('\n')
	oip=[]
	for i in range(len(str1)):
		x=str1[i].find('=')
		oip.append(str1[i][x+2:-1])
	return oip

def sysinfos(mip,part,username,passwd,comm):
	ssh.connect(mip,part,username,passwd)
	stdin, stdout, stderr = ssh.exec_command(comm)
	return stdout
	ssh.close

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

y=openinfo(r"D:\Python27\Scripts\config\rac2.ini")
news = (datetime.datetime.now()).strftime("%Y%m%d")
print "It's :",news

#comm=raw_input("Please iuput commond:")
#vel=raw_input("Please iuput numbers:")
comm='df -hl'
vel=15
rate=sysinfos(y[0],int(y[1]),y[2],y[3],comm)
print ""
for i in range(int(vel)):
	print rate.readline().strip("\n").decode('utf-8').encode('gb2312')
ssh.close