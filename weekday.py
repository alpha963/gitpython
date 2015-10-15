# coding=utf-8
import datetime
todays=[]
for i in range(7):
	y=(datetime.datetime.now() - datetime.timedelta(days = i)).strftime("%Y/%m/%d")
	todays.append(y)
	print todays[i],"00:00"
print todays
to=todays[::-1]
print to







	