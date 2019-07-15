"""
在一个非负整数 a 中，我们希望从中移除 k 个数字，让剩下的数字最小

解决思路：
贪心算法，每次都移除靠进高位最大的数字

Date: 2019-07-15
"""
def min_numbers(num, k):
    num = [i for i in str(num)]
    for i in range(k):
        for i in range(1, len(num)):
            if num[i-1] < num[i]:
                continue
            else:
                num.pop(i-1)
                break
        else:
            num = num.pop()
    return ''.join(num)


print(min_numbers(12432, 2))