"""
选择排序 O(n^2)

需要进行n-1轮比较
"""
def select_sort(alist):
    for i in range(len(alist)-1, 0, -1):
        pos_max = 0
        for j in range(1, i+1):
            if alist[pos_max] < alist[j]:
                pos_max = j
        alist[pos_max], alist[i] = alist[i], alist[pos_max]
    
    return alist

alist = [1,4,2,6,3,0]
print(select_sort(alist))