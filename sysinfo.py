# -*- coding: utf-8 -*-
# coding=utf-8
import paramiko
from openfile import openinfo,comm
import sysinf
import datetime
import sqlite3
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def sysinfos(mip,user,xpasswd,com1,com2,com3,com4):
	ssh.connect(mip,22,user,xpasswd)
	stdin, stdout1, stderr = ssh.exec_command(com1)
	stdin, stdout2, stderr = ssh.exec_command(com2)
	stdin, stdout3, stderr = ssh.exec_command(com3)
	stdin, stdout4, stderr = ssh.exec_command(com4)
	return (stdout1,stdout2,stdout3,stdout4)
	ssh.close

y=openinfo(r"D:\msg\gitpython\gitpython\config\conf.ini")
z=[]
for i in range(len(y)-2):
	z.append(y[i+2])

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

cs=[];frees=[];diss=[];pss=[]

for i in range(9):
	if i<6:
		cpuf,freef,discf,psf=sysinfos(z[i],y[0],y[1],comm[0],comm[2],comm[3],comm[5])
	else:
		cpuf,freef,discf,psf=sysinfos(z[i],y[0],y[1],comm[1],comm[2],comm[4],comm[5])
	p="%.4f" % sysinf.cpuinfo(cpuf,3)
	f="%.4f" % sysinf.freeinfo(freef)
	d=sysinf.discmax(discf,9)
	ps=sysinf.psef(psf)
	cs.append(p)
	frees.append(f)
	diss.append(d)
	pss.append(ps)
ssh.close

cnx = sqlite3.connect("E:/scripts/sqlite3/oipdb.db")
cnx.text_factory = bytes
cur=cnx.cursor()

add_systatus = ("INSERT INTO oip_sys_status VALUES (?,?,?,?,?,?,?)")
oipid=[1,2,3,4,5,6,8,9,10]
dayto = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

for i in range(9):
	cur.execute("select max(id) from oip_sys_status")
	alldata=cur.fetchall()
	t=list(alldata[0])[0]+1
	print cs[i],frees[i],diss[i],dayto,pss[i]
	data_systatus = (t,oipid[i],cs[i],diss[i],frees[i],pss[i],dayto)
	cur.execute(add_systatus, data_systatus)
	emp_no = cur.lastrowid

cnx.commit()
cur.close()
cnx.close()