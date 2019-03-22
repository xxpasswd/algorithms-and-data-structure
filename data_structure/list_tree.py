"""
通过python的嵌套列表实现Tree
"""
import turtle

m = turtle.Turtle()
my = turtle.Screen()
m.speed(0)

def BinaryTree(r):
    return [r, [], []]

def insert_left(root, newbranch):
    """
    向左节点插入时，需要注意左节点是否为空，为空，则插入节点，不为空，需要将左节点的值下降，作为插入节点的左子节点
    """
    t = root.pop(1)
    if len(t) > 0:
        root.insert(1, [newbranch, t, []])
    else:
        root.insert(1, [newbranch, [], []])

def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 0:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])

def get_left_clild(root):
    return root[1]

def get_right_child(root):
    return root[2]

def tree_display(root, n=0):
    """
    可视化树结构
    """
    m.setheading(0)
    m.circle(15)
    m.write(root[0])
    p = m.pos()

    left = root[1]
    right = root[2]
    if left:
        m.setheading(200+n)
        m.forward(100)
        tree_display(left, n+20)
        m.setpos(p)
    if right:
        m.setheading(340-n)
        m.forward(100)
        tree_display(right, n+20)
        m.setpos(p)


root = BinaryTree(1)
insert_left(root, 2)
insert_left(root, 3)
insert_right(get_left_clild(root),6)
insert_right(root, 4)
insert_right(root, 5)
insert_left(get_right_child(root),7)

print(root)
tree_display(root)
my.exitonclick()