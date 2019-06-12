"""
数组实现的队列
操作：
enqueue():O(1)
dequeue():O(1)
"""


class ArrayQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * self.capacity
        self.head = 0
        self.tail = 0

    def enqueue(self, item):
        if self.tail == self.capacity:
            if self.head == 0:
                return False
            else:
                for i in range(0, self.tail-self.head):
                    self.items[i] = self.items[i+self.head]
                self.tail = self.tail - self.head
                self.head = 0

        self.items[self.tail] = item
        self.tail += 1
        return True

    def dequeue(self):
        if self.head == self.tail:
            return None
        temp = self.items[self.head]
        self.head += 1
        return temp


if __name__ == "__main__":
    queue = ArrayQueue(10)
    queue.enqueue(1)
    print(queue.dequeue())
    queue.enqueue(4)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    