import os

fi=[]
for fe in os.listdir(r'c:\Users\qingheng\Documents\NetSarang\Xshell\Logs'):
    fi.append(fe+'\n')
print (fi)
f=open("d:\hello.txt","a+")
f.writelines(fi)
f.close()