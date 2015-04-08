# coding=utf-8
import time
import math
import datetime
weekb=(datetime.datetime.now() - datetime.timedelta(days = 7))
yesterday = (datetime.datetime.now() - datetime.timedelta(days = 1))
y2 = (datetime.datetime.now() - datetime.timedelta(days = 2))
y3 = (datetime.datetime.now() - datetime.timedelta(days = 3))
y4 = (datetime.datetime.now() - datetime.timedelta(days = 4))
y5= (datetime.datetime.now() - datetime.timedelta(days = 5))
y6 = (datetime.datetime.now() - datetime.timedelta(days = 6))

yTime = yesterday.strftime("%Y/%m/%d")
x2=y2.strftime("%Y/%m/%d")
x3=y3.strftime("%Y/%m/%d")
x4=y4.strftime("%Y/%m/%d")
x5=y5.strftime("%Y/%m/%d")
x6=y6.strftime("%Y/%m/%d")
tTime = weekb.strftime("%Y/%m/%d")

print tTime,"\n",x6,"\n",x5,"\n",x4,"\n",x3,"\n",x2,"\n",yTime

for i in range(7):
	print tTime,"00:00"
print ""
for i in range(7):
	print yTime,"00:00"
print yesterday, "test branch"



	