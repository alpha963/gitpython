# coding=utf-8
import math
import datetime
yesterday = (datetime.datetime.now() - datetime.timedelta(days = 1))
print yesterday

def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city

enroll('Sarah', 'F')
enroll('Adam', 'M', city='Tianjin')

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

y=add_end()
z=add_end([5,6])

print y
print z

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

c=calc((1, 3, 5, 7))	
print c

def calcx(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
x=calcx(1,2)
print x

nums = [1, 2, 3]
nu=calcx(*nums)
print nu

def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

kw = {'city': 'Beijing', 'job': 'Engineer'}
wkw=person('Jack', 24, city=kw['city'], job=kw['job'])
print wkw

kw = {'city': 'Tianjin', 'job': 'Porject Manager'}
wqh=person('Aaron', 36, **kw)
print wqh

def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

ffx=func(1, 2, 3, 'a', 'b')
print ffx
ffy=func(1, 2, 3, 'a', 'b', x=99)
print ffy

args = (1, 2, 3, 4,5,'t')
kw = {'x': 99}
ffz=func(*args, **kw)
print ffz