'''
python 实现链表

is_empyt():O(1)
size():O(n)
add(item):O(1)
pop():O(1)
search(item):O(n)
remove(item):O(n)
insert(pos,item):O(n)
'''

class Node:
    def __init__(self,initdata):
        self.node = initdata
        self.next = None

    def get_data(self):
        return self.node

    def get_next(self):
        return self.next

    def set_next(self,newnext):
        self.next = newnext

class LinkList:
    def __init__(self):
        self.head = None

    def is_empyt(self):
        return self.head == None

    def size(self):
        size = 0
        current_node = self.head
        while current_node != None:
            size += 1
            current_node = current_node.get_next()
        return size

    def add(self,item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def pop(self):
        temp = self.head
        if temp != None:
            self.head = temp.get_next()
            return temp
        else:
            return None

    def search(self,item):
        current_node = self.head
        found = False
        while current_node != None:
            if current_node.get_data() == item:
                found = True
                break
            else:
                current_node = current_node.get_next()
        return found

    def remove(self,item):
        current_node = self.head
        previous_node = None 
        while current_node != None:
            if current_node.get_data() == item:
                break
            else:
                previous_node = current_node
                current_node = current_node.get_next()

        if previous_node == None:
            self.head = current_node.get_next()
        else:
            previous_node.set_next(current_node.get_next())        
        
    def insert(self,pos,item):
        current_pos = 0
        previous_node = None
        current_node = self.head
        while current_pos != pos:
            previous_node = current_node
            current_node = current_node.get_next()
            current_pos += 1
        
        temp = Node(item)
        if previous_node == None:
            temp.set_next(current_node)
            self.head = temp
        else:
            previous_node.set_next(temp)
            temp.set_next(current_node)
    

                