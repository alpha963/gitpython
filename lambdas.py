def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
print f
print f()

def count():
    fs = []
    for i in range(1, 3):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2= count()
print f1(),f2()

for i in range(1,3):
	print i

print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
f=lambda x:x*x*x
print f(5)

def builds(x,y):
	return lambda:x*x+y*y
t=builds(1,2)
print t
print t()
