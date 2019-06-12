"""
用单链表实现队列
操作：
enqueue():O(1)
dequeue():O(1)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head == None:
            return None
        else:
            if self.head == self.tail:
                temp = self.head
                self.head = None
                self.tail = None
                return temp.data
            else:
                temp = self.head
                self.head = self.head.next
                return temp.data


if __name__ == "__main__":
    queue = LinkedQueue()
    queue.enqueue(1)
    print(queue.dequeue())
    queue.enqueue(4)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    

