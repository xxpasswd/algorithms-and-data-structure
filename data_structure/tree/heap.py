"""
最小堆：父节点小于左右儿子
操作：
push:O(logn)
pop:O(logn)
heapify:O(n)
"""


class Heap:
    def __init__(self):
        # 添加一个哨兵元素，则左儿子为index*2，右儿子为index*2+1，父节点index//2
        self.size = 0
        self.items = [None]

    def push(self, item):
        self.items.append(item)
        self.size += 1
        self._siftup(self.size)

    def _siftup(self, pos):
        """将当前位置的item上升到合适的位置"""
        while pos // 2 > 0:
            if self.items[pos] < self.items[pos//2]:
                self.items[pos], self.items[pos//2] = self.items[pos//2], self.items[pos]
            pos = pos // 2

    def pop(self):
        item = self.items.pop()
        self.size -= 1
        ret = self.items[1]
        self.items[1] = item
        self._siftdown(1)
        return ret

    def _siftdown(self, pos):
        """将当前位置的item下降到合适的位置"""
        while pos * 2 < self.size + 1:
            min_child = self._get_min_child(pos)
            if self.items[pos] > self.items[min_child]:
                self.items[pos], self.items[min_child] = self.items[min_child], self.items[pos]
            pos = min_child

    def _get_min_child(self, pos):
        left = pos * 2
        right = pos * 2 + 1
        if right < self.size and self.items[right] < self.items[left]:
            return right
        else:
            return left

    def heapify(self, alist):
        self.items = self.items + alist[:]
        self.size = len(alist)
        pos = self.size // 2
        while pos > 0:
            self._siftdown(pos)
            pos -= 1

    def __str__(self):
        return ','.join(map(str, self.items[1:]))


if __name__ == "__main__":
    h = Heap()
    # h.push(5)
    # h.push(2)
    # h.push(3)
    # h.push(4)
    # h.push(10)
    # h.push(7)
    # h.push(1)
    alist = [5,2,3,4,10,7,1]
    h.heapify(alist)    
    print(h)
    print(h.pop())
    print(h)
    print(h.pop())    
    print(h)
    print(h.pop())
    print(h)
    print(h.pop())
    print(h)
    print(h.pop())
    print(h)
    print(h.pop())

