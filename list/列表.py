# -*- coding: utf-8 -*-

L=[123,'spam',1.23]
print len(L)
print L[:-1]
print L+[4,5,6]
L.append('NI')  #尾部插入元素
print L.pop(2)  #取出第三个元素 ，返回值为取出的值
print L
L.sort()   #返回none为完成，查看要在执行后
print L
L.reverse()  #返回none为完成，查看要在执行后
print L
# print L.sort()
# print L.reverse()

