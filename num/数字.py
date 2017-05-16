# -*- coding: utf-8 -*-

print '%4.2f'%(100000/3.0)
print 2*3
print 2**100  #乘方
print len(str(2**100)) #长度

import math,random
print math.pi  #math 常用的数学模块
print math.sqrt(9)
print math.floor(2.5)
print math.trunc(3.4)
print random.random()
print random.randint(0,9)  #随机0-9自然数
print random.choice(['+','-','*','/'])
print sum((1,2,3,4))
print max((1,2,3,4))

import decimal
d=decimal.Decimal('3.141')
d+=1
print d
decimal.getcontext().prec=3  #精确到小数点后两位
print decimal.Decimal('1')/decimal.Decimal('3')

from fractions import Fraction
f=Fraction(2,3)
# f+=1
print f+Fraction(1,2)