'''
给定一个数字，用数组表示，将这个数加1后，返回新的数组
example：[1,0,9] --> [1,1,0],  [1,9,9] --> [2,0,0]

解决思路：
反向遍历数组，每个位数加1后，进行判断
'''

def plus_one(num):
    for i in range(len(num)-1,-1,-1):
        if num[i] < 9:
            num[i] += 1
            return num
        else:
            num[i] = 0
    num.insert(0,1)
    return num


print(plus_one([1,2,3,4]))
