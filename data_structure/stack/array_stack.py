"""
数组实现栈
操作：
push():O(1)
pop():O(1)
"""


class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * self.capacity
        self.top = 0

    def push(self, item):
        if self.top + 1 == self.capacity:
            return False

        self.items[self.top] = item
        self.top += 1
        return True

    def pop(self):
        if self.top == 0:
            return None
        else:
            self.top -= 1
            return self.items[self.top]


if __name__ == "__main__":
    stack = ArrayStack(10)
    stack.push(1)
    stack.push(5)
    stack.push(2)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
