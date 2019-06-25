"""
二叉搜索树
操作：
insert:
get:
delete:
delete_min:
delete_max:
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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
                cur_node.left = TreeNode(value)
        else:
            if cur_node.right:
                self._insert(cur_node.right, value)
            else:
                cur_node.right = TreeNode(value)

    def delete_min(self):
        if self.root == None:
            return None
        elif self.root.left == None:
            self.root = self.root.right
        else:
            self._delete_min(self.root)

    def _delete_min(self, cur_node):
        """需要从删除节点的前一个节点开始判断"""
        if cur_node.left.left == None:
            cur_node.left = cur_node.left.right
        else:
            self._delete_min(cur_node.left)


    def __str__(self):
        return '{}'.format(str(self.root))


if __name__ == "__main__":
    t = BinarySearchTree()
    t.insert(1)
    t.insert(1)
    t.insert(20)
    t.insert(10)
    t.delete_min()
    t.delete_min()
    print(t)
