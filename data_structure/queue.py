'''
python 队列实现

is_empty():O(1)
enqueue(item):O(n)
dequeue(item):O(1)
size():O(1)
'''

class Queue:

    def __init__(self):
        self._queue = []

    def is_empty(self):
        return self._queue == []

    def enqueue(self, item):
        self._queue.insert(0, item)

    def dequeue(self):
        return self._queue.pop()

    def size(self):
        return len(self._queue)

'''
双端队列实现

add_front(item):O(n)
add_rear(item):O(1)
remove_front():O(n)
remove_rear():O(1)
is_empty():O(1)
size():O(1)
'''

class Deque:
    def __init__(self):
        self._deque = []

    def add_front(self, item):
        self._deque.insert(0, item)

    def add_rear(self, item):
        self._deque.append(item)

    def remove_front(self):
        return self._deque.pop(0)

    def remove_rear(self):
        return self._deque.pop()

    def is_empty(self):
        return self._deque == []

    def size(self):
        return len(self._deque)

"""
用双端队列实现回文检测
"""

def palchecker(astring):
    chardeque = Deque()

    for i in astring:
        chardeque.add_rear(i)

    stillequel = True
    while chardeque.size()>1 and stillequel:
        front = chardeque.remove_front()
        rear = chardeque.remove_rear()
        if front != rear:
            stillequel = False

    return stillequel
