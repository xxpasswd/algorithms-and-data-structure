"""
是在插入排序基础上的一种优化排序 O(n)--O(n^2)

shell算法的思想：减少循环的次数
"""
def insert_sort(alist):
    for i in range(1, len(alist)):
        index = i
        for j in range(i-1,-1,-1):
            if alist[j]>alist[index]:
                alist[j],alist[index] = alist[index],alist[j]
                index = j
            else:
                break
    return alist

def gap_insert_sort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        index = i
        for j in range(i-gap, start-gap, -gap):
            if alist[j] > alist[index]:
                alist[j], alist[index] = alist[index], alist[j]
                index = j
            else:
                break
    return alist


def shell_sort(alist):
    sublist_count = len(alist)//2
    while sublist_count > 0:
        for start in range(sublist_count):
            gap_insert_sort(alist, start, sublist_count)
        print(alist)
        sublist_count //= 2
    return alist


        

alist = [3,6,2,1,4,9,5,8,-3]

# print(insert_sort(alist))
print(shell_sort(alist))
