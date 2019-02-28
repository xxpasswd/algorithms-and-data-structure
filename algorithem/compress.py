'''
给出一个字符，对这个字符进行压缩
比如 AAABBCDD  --> A3B2CD2

解决思路：
遍历统计相同字符的个数
'''

def compress(strings):
    prev = strings[0]
    count = 0
    # 输出结果
    out = ''
    for i in strings:
        if i == prev:
            count += 1
        else:
            out += process(prev,count)
            prev = i
            count = 1
    out += process(prev,count)
    return out

def process(s,count):
    if count == 1:
        return s
    else:
        return s + str(count)

print(compress('AAABBCDD'))