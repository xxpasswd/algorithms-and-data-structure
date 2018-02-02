'''
python 队列实现

is_empty():O(1)
enqueue(item):O(n)
dequeue(item):O(1)
size():O(1)
'''

class Queue:
    def __init__(self):
        self.items = []

    
    def is_empty(self):
        return self.items == []

    
    def enqueue(self,item):
        self.items.insert(0,item)

    
    def dequeue(self):
        return self.items.pop()

    
    def size(self):
        return len(self.items)