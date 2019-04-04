"""
通过节点的方式实现树结构
"""
import turtle


class BinaryTree:

    def __init__(self, root_obj):
        self.root = root_obj
        self.left = None
        self.right = None

    def insert_left(self, node):
        if self.left == None:
            self.left = BinaryTree(node)
        else:
            temp = BinaryTree(node)
            temp.left = self.left
            self.left = temp

    def insert_right(self, node):
        if self.right == None:
            self.right = BinaryTree(node)
        else:
            tmep = BinaryTree(node)
            temp.right = self.right
            self.right = tmep

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right


def display(t):
    """可视化这个树结构"""
    global m
    global m_w
    m = turtle.Turtle()
    m_w = turtle.Screen()
    m.speed(0)

    def inner_display(t):
        m.setheading(0)
        m.circle(20)
        m.write(t.root)
        p = m.pos()

        if t.left != None:
            m.setheading(225)
            m.forward(100)
            inner_display(t.left)
            m.setpos(p)

        if t.right != None:
            m.setheading(315)
            m.forward(100)
            inner_display(t.right)
            m.setpos(p)

    inner_display(t)
    m_w.exitonclick()

def preorder(t):
    if t:
        print(t.root)
        preorder(t.get_left_child())
        preorder(t.get_right_child())

def preorder2(t):
    stack = []
    cur_t = t
    while stack or cur_t:
        while cur_t:
            print(cur_t.root)
            stack.append(cur_t)
            cur_t = cur_t.get_left_child()
        
        prev_t = stack.pop()
        cur_t = prev_t.get_right_child() 


def inorder(t):
    if t:
        inorder(t.get_left_child())
        print(t.root)
        inorder(t.get_right_child())


def inorder2(t):
    stack = []
    cur_t = t
    while stack or cur_t:
        while cur_t:
            stack.append(cur_t)
            cur_t = cur_t.get_left_child()

        prev_t = stack.pop()
        print(prev_t.root)
        cur_t = prev_t.get_right_child()


def postorder(t):
    if t:
        postorder(t.get_left_child())
        postorder(t.get_right_child())
        print(t.root)


def hierarchical_traversal(t):
    """
    层序遍历
    主要思路：将树节点一层一层放入队列中，然后取出一个节点的时候，将下一层节点放入队列中
    """
    queue = []
    queue.append(t)
    while queue:
        cur_t = queue.pop(0)
        print(cur_t.root)
        if cur_t.get_left_child():
            queue.append(cur_t.get_left_child())
        if cur_t.get_right_child():
            queue.append(cur_t.get_right_child())



if __name__ == '__main__':
    t = BinaryTree('a')
    t.insert_left('b')
    t.insert_left('c')
    t.insert_right('d')
    inorder(t)
    inorder2(t)
    postorder(t)
    # hierarchical_traversal(t)
    display(t)
