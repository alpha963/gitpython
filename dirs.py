import os

a=r"c:\Users\qingheng\Documents\NetSarang\Xshell\Logs"

fi=[]
for fe in os.listdir(a):
    fi.append(fe+'\n')
print (fi)
print (fe)
#f=open("d:\hello.txt","a+")
#f.writelines(fi)
#f.close()