def cpuinfo(discf,nums):
	cpus=[]
	for i in range(nums):
		s=discf.readline().split()
		cpus.extend(s)
	cpufree=100-float(cpus[0])
	return cpufree

def freeinfo(discf):
	s=discf.readline().split()
	return 1-((float(s[1])+float(s[2]))/float(s[0]))

def discmax(discf,nums):
	app=[];app2=[];r2 = '%';x=0
	
	for i in range(nums):
		s=discf.readline().split()
		app.extend(s)

	for i in range(len(app)):
		if  '%' in app[i]:
			app2.append(int(app[i][:-1]))
		else:
			x=x+1
	return max(app2)

def psef(discf):
	s=discf.readline().split()
	return int(s[0])
