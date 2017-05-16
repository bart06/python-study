# -*- coding: utf-8 -*-

D = {'food':'spam','quantity':4,'color':'pink'}
print D
D['quantity']+=1
print D
DD ={}
DD['name']='Bob'
DD['job']='dev'
DD['age']=40
print DD.keys()
print DD.values()
for k in DD:
    print k,'=>',DD[k]
print  DD.has_key('name')

print dir(DD)