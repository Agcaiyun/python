# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    sqrtNum = b  * b - 4 * a * c
    result1 = (( -b ) + math.sqrt(sqrtNum)) / ( 2 * a)
    result2 = (( -b ) - math.sqrt(sqrtNum)) / ( 2 * a)
    if sqrtNum > 0:
        print('两个不等根：result1 %d' % result1)
        print('两个不等根：result2 %d' % result2)
    elif sqrtNum == 0:
        print('两个相等根：result1=result= %d' % result1 )
    else:
        print('无根')

quadratic(1, 2, 0)