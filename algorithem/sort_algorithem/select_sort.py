"""
选择排序 O(n^2)

需要进行n-1轮比较
"""
def select_sort(alist):
    index = 0
    length = len(alist)
    for i in range(length-1,0,-1):
        for j in range(i):
            if alist[i] < alist[j]:
                alist[i],alist[j] = alist[j], alist[i]

    return alist

alist = [1,4,2,6,3,0]
print(select_sort(alist))