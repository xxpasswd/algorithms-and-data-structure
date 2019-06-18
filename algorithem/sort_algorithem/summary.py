def bubble_sort(a):
    length = len(a)
    for i in range(length):
        for j in range(1, length-i):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
    return a


def select_sort(a):
    for i in range(len(a)):
        max = 0
        for j in range(len(a)-i):
            if a[j] > a[max]:
                max = j
        a[max], a[len(a)-i-1] = a[len(a)-i-1], a[max]
    return a


def insert_sort(a):
    for i in range(1, len(a)):
        pos = i
        while pos > 0 and a[pos] < a[pos-1]:
            a[pos], a[pos-1] = a[pos-1], a[pos]
            pos -= 1
    return a
                

def shell_sort(a):
    count = len(a)//2
    while count > 0:
        for start in range(count):
            gap_insert_sort(a, start, count)
        count = count//2
    return a


def gap_insert_sort(a, start, count):
    for i in range(start, len(a), count):
        pos = i
        while pos > start and a[pos] < a[pos-start]:
            a[pos], a[pos-start] = a[pos-start], a[pos]
            pos -= count


def merge_sort(a):
    if len(a) <=1:
        return a
    mid = len(a)//2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result + left + right 


def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    left = [i for i in a[1:] if i<=pivot]    
    right = [i for i in a[1:] if i>pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)
