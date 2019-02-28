'''
判断两个乱序字符串，是否相同

解决思路：
统计两个字符串中的所有字符的个数，进行逐一对比，若个数都一样，则相同
'''

import string

def anagram(s1:str,s2:str)->"bool":
    # 初始化所有字符的个数
    c1 = {}.fromkeys(string.ascii_letters,0)
    c2 = {}.fromkeys(string.ascii_letters,0)
    
    for i in s1:
        c1[i] += 1

    for i in s2:
        c2[i] += 1

    # 比较两个最后的结果是否一样
    is_same = True
    for key in c1:
        if c2[key] != c1[key]:
            is_same = False
            break
    return is_same

print(anagram('abcde','ecdba'))
