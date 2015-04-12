def odd():
	print 'step 1'
	yield 1
	print 'step 2'
	yield 3
	print 'step 3'
	yield 5
o=odd()
f=[]
for i in o:
	print i

print f

def not_empty(s):
	return s and s.strip()

print filter(not_empty,['A','','B',None,'c','   '])