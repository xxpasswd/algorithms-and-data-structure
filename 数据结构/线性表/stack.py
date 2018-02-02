'''
python 实现栈

is_empty():O(1)
size():O(1)
push(item):O(1)
pop(item):O(1)
'''

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()
