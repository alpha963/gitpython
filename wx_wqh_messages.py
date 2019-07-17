#!/usr/bin/env python
# -*- coding: utf-8 -*-
_author_ = 'GavinHsueh'

import requests
import bs4
import re
import urllib.request
import json
import time;  # 引入time模块
import subprocess

def test():
    str1 = 'ping -c 3 '
    str2 = '192.168.6.100'
    str3 = ' | grep \'0 received\' | wc -l'
    command = str1 + str2 + str3
    print (command)
    p = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
    result = p.stdout.read()
    return result

#--------------------------------
# 获取企业微信token
#--------------------------------

def get_token(url, corpid, corpsecret):
    token_url = '%s/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (url, corpid, corpsecret)
    token = json.loads(urllib.request.urlopen(token_url).read().decode())['access_token']
    return token

#--------------------------------
# 构建告警信息json
#--------------------------------
def messages(msg):
    values = {
        "touser": '@all',
        "msgtype": 'text',
        "agentid": 1000006, #偷懒没有使用变量了，注意修改为对应应用的agentid
        "text": {'content': msg},
        "safe": 0
        }
    msges=(bytes(json.dumps(values), 'utf-8'))
    return msges

#--------------------------------
# 发送告警信息
#--------------------------------
def send_message(url,token, data):
        send_url = '%s/cgi-bin/message/send?access_token=%s' % (url,token)
        respone=urllib.request.urlopen(urllib.request.Request(url=send_url, data=data)).read()
        x = json.loads(respone.decode())['errcode']
        # print(x)
        if x == 0:
            print ('Succesfully')
        else:
            print ('Failed')

##############函数结束########################


#要抓取的目标页码地址
url = 'http://192.168.7.128/GetKey/GetKeyAction.do?opt=getKey'

#抓取页码内容，返回响应对象
response = requests.get(url)

#查看响应状态码
status_code = response.status_code

#使用BeautifulSoup解析代码,并锁定页码指定标签内容
content = bs4.BeautifulSoup(response.content.decode("utf-8"), "lxml")
element = content.find_all(id='today_password')
e2=content.find_all(id='root_today_password')
#x=content.find_all()

#print(status_code)
#print(element)
#print(e2)
mms_index=[re.search('password\"\>', str(element)).span(),re.search('</label>', str(element)).span()]
root_index=[re.search('password\"\>', str(e2)).span(),re.search('</label>', str(e2)).span()]

pw=[str(element)[mms_index[0][1]:mms_index[1][0]],str(e2)[root_index[0][1]:root_index[1][0]]]
#print("今日默认MMS密码：",pw[0])
#print("今日默认root密码：",pw[1])



corpid = 'wwad7173798d430041'
corpsecret = 'Mi3tb3cAJnMm1goKsU3ls0pn2u8Fapyw9MO0ptph6Ig'
url = 'https://qyapi.weixin.qq.com'
tm=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
msg=tm+'\n'+"今日：MMS密码："+pw[0]+'\n'+"今日默认root密码："+pw[1]
#msg='test_user'
#print (str(msg))
#函数调用
test_token=get_token(url, corpid, corpsecret)
msg_data= messages(msg)

a=test().decode()
print(int(a),type(a))

if ( int(a) == 0 ):
   send_message(url,test_token, msg_data)
else:
   print ("今日信息已发送")

