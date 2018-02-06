'''
进制转换
'''

# 递归实现
def base_switch(n,base):
    base_string = '0123456789ABCDEF'
    if n < base:
        return base_string[n]
    else:
        return str(base_switch(n//base,base)) + base_string[n%base]

print(base_switch(15,16))

# 用堆栈实现
def base_switch2(n,base):
    base_string = '0123456789ABCDEF'
    stack = []
    while n > 0:
        if n < base:
            stack.append(base_string[n])
        else:
            stack.append(base_string[n%base])
        n = n//base

    res = ''
    while stack:
        res += stack.pop()
    return res

print(base_switch2(15,16))