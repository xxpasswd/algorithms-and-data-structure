"""
循环队列
操作：
enqueue():
dequeue():

主要是搞清楚head和tail的含义，head是头节点的下标值，tail是下一个要插入节点的下标值
"""


class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity + 1  # 为了代码简洁，我们将容量增大了1
        self.items = [None] * self.capacity
        self.head = 0
        self.tail = 0

    def enqueue(self, item):
        # 当下一个插入节点的下标值 +1 等于head，说明刚好剩一个空间，队列满了
        if (self.tail + 1) % self.capacity == self.head:
            return False

        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        return True

    def dequeue(self):
        if self.head == self.tail:
            return None

        temp = self.items[self.head]
        self.head = (self.head + 1) % self.capacity
        return temp


if __name__ == "__main__":
    queue = CircularQueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    queue.dequeue()
    queue.enqueue(3)
    queue.dequeue()
    queue.enqueue(4)
    queue.dequeue()

