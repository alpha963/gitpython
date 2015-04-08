# coding=utf-8
import time
import math
import datetime
weekb=(datetime.datetime.now() - datetime.timedelta(days = 7))
yesterday = (datetime.datetime.now() - datetime.timedelta(days = 1))

yTime = yesterday.strftime("%Y/%m/%d")

tTime = weekb.strftime("%Y/%m/%d")

print tTime,yTime ,"\n"

print yesterday,weekb