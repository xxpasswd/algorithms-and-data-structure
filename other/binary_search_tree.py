"""
二叉搜索树：
插入
查找
删除
"""
class BinaryTree:
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None
    
    @property
    def root(self):
        return self.value

    def __str__(self):
        return "{{{},{},{}}}".format(self.value, str(self.left), str(self.right))


def insert(t, value):
    if t.value is None:
        t.value = value
    elif value < t.value:
        t.left = t.left if t.left else BinaryTree()
        insert(t.left, value)
    else:
        t.right = t.right if t.right else BinaryTree()
        insert(t.right, value)

def find_pos(t, value):
    if t.value == None:
        return 'Not Fund'
    elif t.value == value:
        return t
    elif value < t.value:
        return find_pos(t.left, value)
    else:
        return find_pos(t.right, value)

def find_max(t):
    if t.right is None:
        return t
    else:
        return find_max(t.right)

def find_min(t):
    if t.left is None:
        return t
    else:
        return find_min(t.left)


def delete(t, value):
    parent, del_t = find_delete_t(t, value)
    if del_t.left is None and del_t.right is None:
        if parent.left == del_t:
            parent.left = None
        else:
            parent.right = None

    elif del_t.left is None:
        if parent.left == del_t:
            parent.left = del_t.right
        else:
            parent.right = del_t.right

    elif del_t.right is None:
        if parent.left == del_t:
            parent.left = del_t.left
        else:
            parent.right = del_t.left
    else:
        min_parent, min_t = find_move_min(del_t.right, del_t)
        del_t.value = min_t.value
        delete(min_parent, value)


def find_delete_t(t, value, parent_t=None):
    if t.value == None:
        return parent_t, None
    elif value == t.value:
        return parent_t, t
    elif value < t.value:
        return find_delete_t(t.left, value, t)
    else:
        return find_delete_t(t.right, value, t)

def find_move_min(t, parent_t=None):
    if t.left is None:
        return parent_t, t
    else:
        return find_move_min(t.left, t)
        
        
if __name__ == "__main__":
    t = BinaryTree(5)
    insert(t, 4)
    insert(t, 2)
    insert(t, 6)
    insert(t, 3)
    print(t)
    delete(t, 4)
    print(t)
