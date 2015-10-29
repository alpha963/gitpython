# coding=utf-8
import math

def quadratic(a,b,c):
	x=(-b+(math.sqrt(b*b-4*a*c)))/(2*a)
	y=(-b-math.sqrt(b*b-4*a*c))/(2*a)
	return x,y

def power(x,n):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s

print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))
print (power(2,8))	