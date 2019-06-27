"""
二叉搜索树
操作：
insert:O(logn)
get:O(logn)
delete:O(logn)
delete_min:O(logn)
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return '{{{},{},{}}}'.format(self.value, str(self.left), str(self.right))


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, cur_node, value):
        if cur_node.value >= value:
            if cur_node.left:
                self._insert(cur_node.left, value)
            else:
                new_node = TreeNode(value)
                self._set_node(cur_node, new_node, 'left')
        else:
            if cur_node.right:
                self._insert(cur_node.right, value)
            else:
                new_node = TreeNode(value)
                self._set_node(cur_node, new_node, 'right')

    def _set_node(self, parent, child, direction):
        """给parent节点的左节点或右节点赋值"""
        if parent:
            setattr(parent, direction, child)
            if child:
                child.parent = parent
        else:
            # 只有root的parent为None
            self.root = child
            if self.root:
                self.root.parent = None

    def delete_min(self):
        if self.root == None:
            return None
        else:
            min_node = self._get_min(self.root)
            parent = min_node.parent
            self._set_node(parent, min_node.right, 'left')
            return min_node

    def get(self, value):
        if self.root == None:
            return None
        else:
            return self._get(self.root, value)

    def _get(self, cur_node, value):
        if cur_node == None:
            return None
        elif cur_node.value == value:
            return cur_node
        elif cur_node.value < value:
            return self._get(cur_node.right, value)
        elif cur_node.value > value:
            return self._get(cur_node.left, value)

    def delete(self, value):
        if self.root == None:
            return None
        else:
            return self._delete(self.root, value)
    
    def _delete(self, cur_node, value):
        if cur_node == None:
            return None
        elif cur_node.value == value:
            if cur_node.left == None and cur_node.right == None:
                self._delete_node(cur_node, None)
            elif cur_node.right == None:
                self._delete_node(cur_node, cur_node.left)
            elif cur_node.left == None:
                self._delete_node(cur_node, cur_node.right)
            else:
                move_node = self._get_min(cur_node.right)
                self._delete(move_node, None)
                self._set_node(move_node, cur_node.left, 'left')
                self._set_node(move_node, cur_node.right, 'right')
                self._delete(cur_node, move_node)
            return cur_node
        elif value < cur_node.value:
            return self._delete(cur_node.left, value)
        else:
            return self._delete(cur_node.right, value)

    def _delete_node(self, cur_node, child):
        if cur_node.parent:
            if cur_node.parent.left == cur_node:
                self._set_node(cur_node.parent, child, 'left')
            else:
                self._set_node(cur_node.parent, child, 'right')
        else:
            # root节点的parent为None
            self.root = child
            self.root.parent = None

    def _get_min(self, cur_node):
        if cur_node.left == None:
            return cur_node
        else:
            return self._get_min(cur_node.left)

    def __str__(self):
        return '{}'.format(str(self.root))


if __name__ == "__main__":
    t = BinarySearchTree()
    t.insert(1)
    t.insert(1)
    t.insert(20)
    t.insert(10)
    t.delete_min()
    print(t)
    t.delete(10)
    t.delete(20)
    print(t)
