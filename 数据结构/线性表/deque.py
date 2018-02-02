"""
python 双端队列实现

is_empty()：O(1)
size()：O(n)
add_front(item):O(1)
add_rear(item):O(n)
remove_front():O(1)
remove_rear():O(n)
"""

class Deque:
    def __init__(self):
        self.deque = []

    def is_empty(self):
        return self.deque == []

    def size(self):
        return len(self.deque)

    def add_front(self,item):
        self.deque.append(item)

    def add_rear(self,item):
        self.deque.insert(0,item)

    def remove_front(self):
        self.deque.pop()

    def remove_rear(self):
        self.deque.pop(0)
