"""
通过节点的方式实现树结构
"""
import turtle

m = turtle.Turtle()
m_w = turtle.Screen()
m.speed(0)


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

    def display(self):
        """可视化这个树结构"""
        m.setheading(0)
        m.circle(20)
        m.write(self.root)
        p = m.pos()

        if self.left != None:
            m.setheading(225)
            m.forward(100)
            self.left.display()
            m.setpos(p)

        if self.right != None:
            m.setheading(315)
            m.forward(100)
            self.right.display()
            m.setpos(p)

if __name__ == '__main__':
    t = BinaryTree('a')
    t.insert_left('b')
    t.insert_left('c')
    t.insert_right('d')
    t.display()       
    m_w.exitonclick()
