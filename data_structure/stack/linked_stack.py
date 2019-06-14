"""
用链表实现栈
操作：
push():O(1)
pop():O(1)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        if self.top == None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.top == None:
            return None
        temp = self.top
        self.top = self.top.next
        return temp.data

    def is_empty(self):
        if self.top == None:
            return True
        return False

    def first(self):
        if self.top == None:
            return None
        
        return self.top.data

    def __str__(self):
        temp = self.top
        res = ''
        while temp:
            res += temp.data
            temp = temp.next
        return res[::-1]

if __name__ == "__main__":
    stack = LinkedStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
