"""
双向链表
操作：
insert_to_head():O(1)
insert_to_tail():O(1)
delete_head():O(1)
delete_tail():O(1)
find_by_value():O(n)
delete_by_value():O(n)
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.pre = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_to_head(self, value):
        """从头部插入一个节点"""
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.pre = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_to_tail(self, value):
        """从尾部插入一个节点"""
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.pre = self.tail
            self.tail = new_node

    def delete_head(self):
        """从头部删除一个节点"""
        if self.head == None:
            return None

        temp = self.head
        self.head = self.head.next
        self.head.pre = None
        if self.head == None:
            self.tail = None
        temp.next = None
        return temp

    def detele_tail(self):
        """从尾部删除一个节点"""
        if self.head == None:
            return None

        temp = self.tail
        self.tail = self.tail.pre
        self.tail.next = None
        if self.tail == None:
            self.head = None
        temp.pre = None
        return temp

    def find_by_value(self, value):
        """通过值查询节点"""
        temp = self.head
        while temp and temp.value != value:
            temp = temp.next
        return temp

    def delete_by_value(self, value):
        """通过值删除节点"""
        temp = self.head
        while temp and temp.value != value:
            temp = temp.next
        
        if temp == None: 
            return None
        
        pre_node = temp.pre
        next_node = temp.next
        pre_node.next = next_node
        next_node.pre = pre_node
        temp.pre, temp.next = None, None
        return temp

