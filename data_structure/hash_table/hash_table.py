"""
开放寻址和线性探测的哈希表

设计一个高可用哈希表的注意点：
1. 装载因子
2. 动态扩容
3. 哈希函数
"""

import pysnooper

class HashTable:
    def __init__(self):
        self.size = 10
        self.slot = [None] * self.size
        self.keys = [None] * self.size

    def put(self, key, value):
        index = self.hash(key)
        if self.slot[index] == None:
            self.keys[index] = key
            self.slot[index] = value
        elif self.keys[index] == key:
            self.slot[index] = key
        else:
            colision_solution = self._colision_solution(key, index)
            if colision_solution is not None:
                self.keys[colision_solution] = key
                self.slot[colision_solution] = value
            else:
                # 说明空间满了，进行扩容
                self.rehasing()
                self.put(key, value)

    def get(self, key):
        index = self.hash(key)
        start = index
        while self.keys[index] is not None and self.keys[index] != key:
            index = self.hash(index+1)
            if index == start:
                break
        if self.keys[index] == None:
            raise Exception('Not Fund!')
        elif self.keys[index] == key:
            return self.slot[index]
        else:
            raise Exception('Not Fund!')

    def hash(self, key):
        return key % self.size

    def rehasing(self):
        keys = self.keys
        slot = self.slot
        size = self.size
        self.size = self.size * 2
        self.keys = [None] * self.size
        self.slot = [None] * self.size
        for i in range(size):
            self.put(keys[i], slot[i])

    def _colision_solution(self, key, index):
        index = self.hash(index+1)
        new_key = index
        while self.slot[index] != None and self.keys[index] != key:
            if self.slot.count(None) > 0:
                index = self.hash(index+1)
                new_key = index
            else:
                new_key = None
                break
        return new_key

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, item):
        self.put(key, item)


if __name__ == "__main__":
    from random import randint
    from itertools import chain
    h = HashTable()
    t = [2, 5, 87, 66, 28, 52, 26, 85]
    t2 = [17, 198, 262, 252, 148, 298, 275, 177, 41, 56]
    for i in t:
        h.put(i, i)

    for i in t2:
        h.put(i, i)

    for i in chain(t2, t):
        print(h.get(i))

