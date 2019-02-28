"""
最小差:
给出两个数组，从两个数组中各取一个元素，两者差值越小越好

思路：
将一个数组排序后，遍历第二个数组到第一个数组二分，判断二分位置附近的差值，找出最小
"""

a=[4,3,5,7]
b=[2,3,8,9]

a.sort()
b.sort()

# m是a的下标，n是b的下标
m,n=0,0
res = 99999

while True:
    res = abs(a[m]-b[n]) if res>abs(a[m]-b[n]) else res
    if a[m]<b[n]:
        m += 1
    elif a[m]>b[n]:
        n += 1
    else:
        break

print(m,n)

