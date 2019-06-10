"""
单链表：
insert_to_head():O(1)
insert_to_tail():O(n)
delete_head():O(1)
delete_tail():O(n)
find_by_value():O(n)
find_by_index():O(n)
insert_after():O(1)
delete_by_value():O(n)
reverse():O(n)
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_to_head(self, value):
        """从头部插入"""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_to_tail(self, value):
        """从尾部插入，找到最后一个节点后进行插入"""
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node

    def delete_head(self):
        """从头部删除一个节点"""
        temp = self.head
        if temp != None:
            self.head = temp.next
            temp.next = None
        return temp

    def delete_tail(self):
        """从尾部删除一个节点，需要找到最后一个节点的前一个节点"""
        temp = self.head
        if temp == None:
            return temp
        elif temp.next == None:
            self.head = None
            return temp
        else:
            while temp.next.next != None:
                temp = temp.next
            temp.next, temp = None, temp.next
            return temp
        
    def find_by_value(self, value):
        """通过值查找节点"""
        temp = self.head
        if temp == None:
            return None
        while temp != None and temp.data != value:
            temp = temp.next
        return temp

    def find_by_index(self, index):
        """通过索引查找节点"""
        temp = self.head
        pos = 0
        while temp != None and pos != index:
            temp = temp.next
            pos += 1
        return temp

    def insert_after(self, node, value):
        """在链表的指定节点后面插入一个节点"""
        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node
    
    def insert_before(self, node, value):
        """在链表的指定节点前面插入一个节点，需要找到指定节点的前一个节点"""
        pass

    def delete_by_value(self, value):
        """通过值删除节点，需要找到要删除节点的前一个节点"""
        temp = self.head
        if temp == None:
            return None
        elif temp.next == None:
            if temp.data == value:
                self.head = None
                temp.next = None
                return temp
            else:
                return None
        else:
            while temp.next.next != None:
                if temp.next.data == value:
                    break
                temp = temp.next
            if temp.next.data == value:
                temp.next, temp = temp.next.next, temp.next
                temp.next = None
                return temp
            else:
                return None

    def reverse(self):
        """反转链表"""
        if self.head == None or self.head.next == None:
            return
        pro = self.head
        node = self.head.next
        pro.next = None
        while node != None:
            temp = node.next
            node.next = pro
            pro = node
            node = temp

        self.head = pro

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=',')
            temp = temp.next        
        print()


if __name__ == "__main__":
    l = SinglyLinkedList()
    l.insert_to_head(1)
    l.print_list()

    l.insert_to_head(2)
    l.insert_to_head(3)
    l.print_list()
    
    l.insert_to_tail(4)
    l.insert_to_tail(5)
    l.print_list()
    
    l.delete_head()
    l.print_list()

    l.delete_tail()
    l.print_list()

    l.delete_by_value(1)
    l.print_list()

    l.reverse()
    l.print_list()
