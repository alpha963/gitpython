def openinfo(filenam):
	infoip= open(filenam)  
	try:
		text = infoip.read( )  
	finally:
		infoip.close( ) 
	str1=text.split('\n')
	oip=[]
	for i in range(len(str1)):
		x=str1[i].find('=')
		oip.append(str1[i][x+2:-1])
	return tuple(oip)