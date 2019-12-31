# -*- coding: utf-8 -*-

def trim(s):
    if len(s) == 0:
        s = ''
    else :
        if s[0] == ' ' :
            return trim(s[1:])
        if s[-1] == ' ' :
            return trim(s[: -1])
    
    return s

if trim('hello  ') != 'hello':
    print('hello  测试失败!')
elif trim('  hello') != 'hello':
    print('  hello测试失败!')
elif trim('  hello  ') != 'hello':
    print('  hello  测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('  hello  world  测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('    测试失败!')
else:
    print('测试成功!')