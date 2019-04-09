class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return '{{{},{},{}}}'.format(self.val, str(self.left), str(self.right))


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if not self.root:
            self.root = TreeNode(key, val)
        else:
            self._put(key, val, self.root)
        self.size += 1

    def _put(self, key, value, cur_node):
        if cur_node.val > value:
            if cur_node.left:
                self._put(key, value, cur_node.left)
            else:
                cur_node.left = TreeNode(key, value, parent=cur_node)
        else:
            if cur_node.right:
                self._put(key, value, cur_node.right)
            else:
                cur_node.right = TreeNode(key, value, parent=cur_node)
        
    def get(self, value):
        if self.root is None:
            return None
        else:
            return self._get(value, self.root)

    def _get(self, value, cur_node):
        if cur_node.val == value:
            return cur_node
        elif cur_node.val > value:
            return self._get(value, cur_node.left) if cur_node.left else None
        else:
            return self._get(value, cur_node.right) if cur_node.right else None

    def delete(self, value):
        del_node = self.get(value)
        if del_node is not None:
            if del_node.left is None and del_node.right is None:
                if del_node.parent.left == del_node:
                    del_node.parent.left = None
                else:
                    del_node.parent.right = None
            elif del_node.right is None:
                if del_node.parent.left == del_node:
                    del_node.parent.left = del_node.left
                else:
                    del_node.parent.right = del_node.left
            elif del_node.left is None:
                if del_node.parent.left == del_node:
                    del_node.parent.left = del_node.right
                else:
                    del_node.parent.right = del_node.right
            else:
                min_node = self.get_min_node()
                self.delete_min(min_node)
                del_node.key = min_node.key
                del_node.val = min_node.val

    def get_min_node(self):
        # 获取最小的叶子节点
        return self._get_min_node(self.root)

    def _get_min_node(self, cur_node):
        if cur_node.left:
            return self._get_min_node(cur_node.left)
        else:
            return cur_node

    def delete_min(self, min_node):
        # 删除最小节点
        if min_node.left is None and min_node.right is None:
            if min_node.parent.left == min_node:
                min_node.parent.left = None
            else:
                min_node.parent.right = None
        elif min_node.left is None:
            if min_node.parent.left == min_node:
                min_node.parent.left = min_node.right 
            else:
                min_node.parent.right = min_node.right
        else:
            if min_node.parent.left == min_node:
                min_node.parent.left = min_node.left
            else:
                min_node.parent.right = min_node.right

    def __str__(self):
        return '{}'.format(str(self.root))

if __name__ == "__main__":
    t = BinarySearchTree()
    t.put(2,3)
    t.put(2,4)
    t.put(2,5)
    t.put(2,1)
    print(t)
    t.delete(3)
    print(t)