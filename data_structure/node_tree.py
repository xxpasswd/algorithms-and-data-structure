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

    def inner_display(self):
        m.setheading(0)
        m.circle(20)
        m.write(self.root)
        p = m.pos()

        if self.left != None:
            m.setheading(225)
            m.forward(100)
            self.left.inner_display()
            m.setpos(p)

        if self.right != None:
            m.setheading(315)
            m.forward(100)
            self.right.inner_display()
            m.setpos(p)

    def display(self):
        """可视化这个树结构"""
        global m
        global m_w
        m = turtle.Turtle()
        m_w = turtle.Screen()
        m.speed(0)
        self.inner_display()
        m_w.exitonclick()

def preorder(t):
    if t:
        print(t.root)
        preorder(t.get_left_child())
        preorder(t.get_right_child())


def inorder(t):
    if t:
        inorder(t.get_left_child())
        print(t.root)
        inorder(t.get_right_child())


def postorder(t):
    if t:
        postorder(t.get_left_child())
        postorder(t.get_right_child())
        print(t.root)


if __name__ == '__main__':
    t = BinaryTree('a')
    t.insert_left('b')
    t.insert_left('c')
    t.insert_right('d')
    # preorder(t)  
    inorder(t)     
    # t.display()

