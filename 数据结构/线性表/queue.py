'''
python 队列实现

is_empty():O(1)
enqueue():O(n)
dequeue():O(1)
size():O(1)

'''

class Queue(object):
    def __init__(self):
        self._items = []

    
    def is_empty(self):
        return self._items == []

    
    def enqueue(self,item):
        self._items.insert(0,item)

    
    def dequeue(self):
        return self._items.pop()

    
    def size(self):
        return len(self._items)