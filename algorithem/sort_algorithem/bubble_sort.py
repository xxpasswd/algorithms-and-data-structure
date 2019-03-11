"""
冒泡排序 O(n2)

需要进行n-1轮排序
"""
def bubble_sort(alist):
    length = len(alist)

    for i in range(length-1):
        end = length-1-i
        start = 0

        while start < end:
            if alist[start] > alist[start+1]:
                alist[start], alist[start+1] = alist[start+1], alist[start]
            start += 1

    return alist

def shor_bubble_sort(alist):
    passnums = len(alist)-1
    exchange = True
    
    while passnums > 0 and exchange:
        exchange = False
        for i in range(passnums):
            if alist[i] > alist[i+1]:
                alist[i+1],alist[i] = alist[i],alist[i+1]
                exchange = True
        passnums -= 1
    return alist
    

alist = [5,9,0,3,7,4]
print(bubble_sort(alist))
print(shor_bubble_sort(alist))