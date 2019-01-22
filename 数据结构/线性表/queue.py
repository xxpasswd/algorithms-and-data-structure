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