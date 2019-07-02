"""
堆排序 O(nlogn)

先建堆，然后一步步取出堆顶元素
"""

from heapq import _heapify_max


def heap_sort(alist):
    _heapify_max(alist)
    print(alist)
    for n in range(len(alist)-1, 0, -1):
        alist[0], alist[n] = alist[n], alist[0]
        _siftdown(alist, 0, n-1)
    return alist


def _siftdown(heap, pos, endpos):
    endpos =  endpos
    childpos = 2*pos + 1
    while childpos <= endpos:
        rightpos = childpos + 1
        if rightpos <= endpos and heap[rightpos] > heap[childpos]:
            childpos = rightpos

        if heap[pos]<heap[childpos]:
            heap[pos], heap[childpos] = heap[childpos], heap[pos]
        else:
            break
        
        pos = childpos
        childpos = 2*pos+1

alist = [5,10,7,2,3,1,-5]    
alist = heap_sort(alist)
print(alist)   
