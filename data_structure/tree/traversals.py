"""
二叉树遍历：
先序遍历:
    先输出一个节点自身，然后是左节点，最后是右节点
中序遍历：
    先输出一个节点左节点，然后是自身，最后是右节点
后序遍历：
    先输出一个节点的左节点，然后是右节点，最后是自身
"""


from binary_search_tree import BinarySearchTree


def pre_order(t):
    if t:
        print(t.value)
        pre_order(t.left)
        pre_order(t.right)


def pre_order2(t):
    stack = []
    stack.append(t)
    while stack:
        t = stack.pop()
        print(t.value)
        if t.right:
            stack.append(t.right)
        if t.left:
            stack.append(t.left)


def in_order(t):
    if t:
        in_order(t.left)
        print(t.value)
        in_order(t.right)


def in_order2(t):
    stack = []
    while stack or t:
        while t:
            stack.append(t)
            t = t.left
        t = stack.pop()
        print(t.value)
        t = t.right
    

def post_order(t):
    if t:
        post_order(t.left)
        post_order(t.right)
        print(t.value)


def post_order2(t):
    stack = []
    last_visit = None
    while t:
        stack.append(t)
        t = t.left
    while stack:
        t = stack.pop()
        if t.right and last_visit != t.right:
            stack.append(t)
            t = t.right
            while t:
                stack.append(t)
                t = t.left
        else:
            print(t.value)
            last_visit = t


def hierarchical_traversals(t):
    queue = []
    queue.append(t)
    while queue:
        t = queue.pop(0)
        print(t.value)
        if t.left:
            queue.append(t.left)
        if t.right:
            queue.append(t.right)

if __name__ == "__main__":
    t = BinarySearchTree()
    # {10,{5,{3,None,None},{8,None,None}},{15,{13,None,None},{17,None,None}}}
    t.insert(10)
    t.insert(5)
    t.insert(8)
    t.insert(3)
    t.insert(15)
    t.insert(13)
    t.insert(17)
    print(t)
    # pre_order(t.root)
    # in_order(t.root)
    # post_order(t.root)
    # pre_order2(t.root)
    # in_order2(t.root)
    post_order2(t.root)
    # hierarchical_traversals(t.root)
