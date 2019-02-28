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
