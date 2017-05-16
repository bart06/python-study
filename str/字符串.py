# -*- coding: utf-8 -*-

s='Spam'
print type(s)
print len(s)
print s[0]
print s[-2] #倒数第二个数字
print s[:3]
print s[:-1]
print s+'xyz'

print '----------ASCII---------'
print ord('\n')
print str(chr(56))

print '-----------方法-----------'
print dir(s)         #查看对象的方法和属性
print s.upper()
print s.isalpha()
print s.find('pa')  #查找对应的位置
print s.replace('pa','XYZ')  #替换字符串对应的位置

line = 'aaa,bbb,ccc,dd'
nline=line.split(',')
print nline
print help(s.replace)

print '-----------格式化-------------'
print '%s,egg,and %s' %('spam','SPAM!')
print  '{0},egg,and {1}'.format('spam','SPAM!')

