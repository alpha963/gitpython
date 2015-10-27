#coding=utf-8
#python2.7.10
import datetime

def openinfo(filenam):
	infoip= open(filenam)  
	try:
		text = infoip.read( )  
	finally:
		infoip.close( ) 
	str1=text.split('\n')
	oip=[]
	for i in range(len(str1)):
		oip.append(str1[i])
	return oip

y=openinfo("C:\Users\qingheng\Documents\NetSarang\Xshell\Logs\samsung.log")
news = (datetime.datetime.now()).strftime("%Y%m%d")
print ("It's :",news)

t=[]
for i in range(len(y)):
	x=y[i].find('ConsoleMessage')
	if x!=-1:
		t.append(y[i])
	else:
		pass

for i in range(len(t)):
	print (t[i])
print ('Connection closed in finally\n')



