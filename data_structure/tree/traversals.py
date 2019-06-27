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
    t.insert(5)
    t.insert(4)
    t.insert(6)
    t.insert(3)
    t.insert(7)
    t.insert(2)
    t.insert(8)
    print(t)
    # pre_order(t.root)
    # in_order(t.root)
    # post_order(t.root)
    # pre_order2(t.root)
    in_order2(t.root)
    # hierarchical_traversals(t.root)
