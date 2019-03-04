"""
线性搜索:O(n)
"""

def sequential_search(alist, item):
    i = 0
    found = False
    while i < len(alist) and not found:
        if alist[i] == item:
            found = True
        i += 1
    return found

print(sequential_search([1,2,3,4,5], 6))

def order_sequential_search(alist, item):
    i = 0
    found = False
    while i < len(alist) and not found:
        if alist[i] == item:
            found = True
        elif alist[i] > item:
            break
        i += 1
    return found


def binary_search(alist, item):
    start, end = 0, len(alist)-1
    mid = (start + end) // 2
    found = False
    while start < end-1 and not found:
        if item[mid] < item:
            start = mid
        elif item[mid] > item:
            end = mid
        else:
            found = True
        mid = (start + end) // 2
    return found