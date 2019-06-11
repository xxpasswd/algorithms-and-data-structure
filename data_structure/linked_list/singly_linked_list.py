"""
单链表：
insert_to_head():O(1)
insert_to_tail():O(n)
delete_head():O(1)
delete_tail():O(n)
find_by_value():O(n)
find_by_index():O(n)
insert_after():O(1)
insert_before():O(n)
delete_by_node():O(n)
delete_by_value():O(n)
delete_last_N_node():O(n)
delete_last_Nth_node():O(n)
reverse():O(n)
find_mid_node():O(n)
has_ring():O(n)
is_palindrome():O(n)
swap_node():O(n)
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
        if node == None:
            return

        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node
    
    def insert_before(self, node, value):
        """在链表的指定节点前面插入一个节点，需要找到指定节点的前一个节点"""
        if node == None:
            return

        if node == self.head:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

        while temp:
            if temp.next == node:
                break
            temp = temp.next
        if temp == None:
            return
        else:
            new_node = Node(value)
            new_node.next = temp.next
            temp.next = new_node

    def delete_by_node(self, node):
        """通过节点删除，需要找到删除节点的前一个节点"""
        if node == None:
            return None
        
        if self.head == None:
            return None
        
        if self.head == node:
            self.head = self.head.next
            return node

        pro = self.head
        cur = self.head.next
        while cur:
            if cur == node:
                break
            pro = cur
            cur = cur.next
        if cur == None:
            return None
        else:
            pro.next = cur.next
            cur.next = None
            return cur
        
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

    def delete_last_N_node(self, n):
        """删除最后n个节点"""
        fast = self.head
        slow = self.head
        step = 0
        while step != n:
            fast = fast.next
            step += 1

        while fast.next != None:
            fast = fast.next
            slow = slow.next
        temp = slow.next
        slow.next = None
        return temp

    def delete_last_Nth_node(self, n):
        """删除倒数第n个节点"""
        fast = self.head
        slow = self.head
        step = 0
        while step != n:
            fast = fast.next
            step += 1

        while fast.next != None:
            fast = fast.next
            slow = slow.next
        temp = slow.next
        slow.next = slow.next.next
        return temp

    def reverse(self):
        """反转链表"""
        if self.head == None or self.head.next == None:
            return
        pro = self.head
        cur = self.head.next
        pro.next = None
        while cur != None:
            temp = cur.next    # 先把当前节点后面的节点记下来  
            cur.next = pro     # 让当前节点的下一个指向前一个节点
            pro = cur         # 当前节点成为下一次遍历的前一个节点
            cur = temp         # 继续遍历剩下的节点

        self.head = pro

    def find_mid_node(self):
        """查找中间节点，慢指针返回的位置是中间或者中间的第二个元素"""
        fast = self.head
        slow = self.head
        while fast and fast.next:
            print(fast.data, slow.data)
            fast = fast.next.next
            slow = slow.next
        return slow

    def has_ring(self):
        """判断链表是否有环"""
        fast = self.head
        slow = self.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    def is_palindrome(self):
        """判断是否是回文"""
        fast = self.head
        slow = self.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        stack = []
        while slow:
            stack.append(slow.data)
            slow = slow.next

        temp = self.head
        is_palindrome = True
        while temp and stack:
            if temp.data != stack.pop():
                is_palindrome = False
                break
            temp = temp.next
        return is_palindrome

    def swap_node(self, v1, v2):
        """交换两个节点，需要找到交换节点的前一个节点"""
        if v1 == v2:
            return
        
        prev_d1 = None
        prev_d2 = None

        # 查找v1
        d1 = self.head
        while d1 and d1.data != v1:
            prev_d1 = d1
            d1 = d1.next

        # 查找v2
        d2 = self.head
        while d2 and d2.data != v2:
            prev_d2 = d2
            d2 = d2.next

        



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
    l.insert_to_tail(6)
    l.print_list()

    a = l.find_mid_node()
    print(a.data)   
    l.delete_last_Nth_node(3)
    l.print_list()

    l.delete_head()
    l.print_list()

    l.delete_tail()
    l.print_list()

    l.delete_by_value(1)
    l.print_list()

    l.reverse()
    l.print_list()

    l.insert_to_head(5)
    l.insert_to_head(2)
    l.print_list()
    b = l.is_palindrome()
    print(b)
