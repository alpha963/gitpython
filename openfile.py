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

comm=("mpstat|awk  '{if($11!~/idle/) print $11}'","mpstat|awk  '{if($12!~/idle/) print $12}'",\
"free -m|awk  '{if($1!~/total/) print $2,$4,$7}'|head -1",\
"df -hl|awk  '{if($5!~/Use/) print $3,$4,$5}'","df -hl|awk  '{if($5!~/Use/) print $4,$5,$6}'",\
"ps -ef|wc -l")