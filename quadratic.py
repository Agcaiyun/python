# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    sqrtNum = b  * b - 4 * a * c
    result1 = (( -b ) + math.sqrt(sqrtNum)) / ( 2 * a)
    result2 = (( -b ) - math.sqrt(sqrtNum)) / ( 2 * a)
    print(sqrtNum)
    print(result1)
    print(result2)

    if sqrtNum > 0:
        print('两个不等根：result1: %.1f, result2: %.1f' % (result1, result2))
    elif sqrtNum == 0:
        print('两个相等根：result1=result= %.1f' % result1 )
    else:
        print('无根')