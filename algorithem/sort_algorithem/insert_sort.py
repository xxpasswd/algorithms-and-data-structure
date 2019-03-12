"""
插入排序 O(n^2)

需要进行n-1轮
"""
def insert_sort(alist):
    length = len(alist)
    for i in range(1,length):
        index = i
        while index > 0:
            if alist[index] < alist[index-1]:
                alist[index], alist[index-1] = alist[index-1], alist[index]
                index -= 1
            else:
                break
    return alist

alist = [5,9,0,3,7,4]
print(insert_sort(alist))