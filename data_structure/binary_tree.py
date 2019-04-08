class BinaryTree:
    def __init__(self):
        self.heaplist = [0]
        self.size = 0

    def insert(self, value):
        self.heaplist.append(value)
        self.size += 1
        self.percolate_up()

    def delete_min(self):
        self.size -= 1
        temp = self.heaplist[1]
        self.heaplist[1] = self.heaplist.pop()
        self.percolate_down()
        return temp

    def build_heap(self, alist):
        i = len(alist)//2
        self.heaplist = self.heaplist + alist
        self.size = len(self.heaplist)
        while i > 0:
            self.percolate_down(i)
            i = i-1

    def percolate_up(self):
        i = self.size
        parent = i//2
        while parent > 0:
            if self.heaplist[parent] > self.heaplist[i]:
                self.heaplist[parent], self.heaplist[i] = self.heaplist[i], self.heaplist[parent]
                i = parent
                parent = parent//2
            else:
                break

    def percolate_down(self):
        i = 1
        while i*2+1 <= self.size:
            mc = self.min_chlid(i)
            if self.heaplist[mc] < self.heaplist[i]:
                self.heaplist[mc], self.heaplist[i] = self.heaplist[i], self.heaplist[mc]
                i = mc
            else:
                break

    def min_chlid(self,i):
        if i*2+1 < self.size:
            return i*2
        else:
            if self.heaplist[i*2] < self.heaplist[i*2+1]:
                return i*2
            else:
                return i*2+1

    
    def __str__(self):
        return "{}".format(self.heaplist)

if __name__ == "__main__":
    h = BinaryTree()
    h.insert(2)
    h.insert(3)
    h.insert(4)
    h.insert(1)
    print(h)