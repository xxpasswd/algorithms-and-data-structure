"""
python用堆实现递归，将要调用的函数压入堆中，最后再依次返回

递归的三个定律：
1. 必须有一个最基本的案例
2. 每次递归调用，必须向最基本的案例靠近
3. 递归调用自己
"""

# 递归求一个列表的和
def add(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + add(l[1:])

l = [1,2,3,4]
print(add(l))


# 进制转换的非递归实现
def tostr(n, base):
    base_string = '0123456789ABCEDF'
    stack = []

    while n >= base:
        r = n%base
        stack.append(r)
        n = n//base
    stack.append(n)
    
    res = ''
    while stack:
        s = base_string[stack.pop()]
        res += s

    return res

# 进制转换的递归实现
def tostr2(n, base):
    base_string = '0123456789ABCEDF'
    
    if n < base:
        return base_string[n]
    else:
        return tostr2(n//base, base) + base_string[n%base]

print(tostr2(4,2))

# 递归实现字符串反转
def reverse(string):
    if len(string) == 1:
        return string
    else:
        return reverse(string[1:]) + string[0]
