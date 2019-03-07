"""
一个简单的hash map
"""
class HashTable:
    SZIE = 2

    def __init__(self):
        self.key = [None] * self.SZIE
        self.data = [None] * self.SZIE

    def put(self, key, data):
        assert isinstance(key, int)
        index = self.hash_function(key)
        if self.key[index] == None:
            self.key[index] = key
            self.data[index] = data
        else:
            if self.key[index] == key:
                self.data[index] = data  # 替换值
            else:
                start = index
                index = self.re_hashing(index)
                while self.key[index] != None and self.key[index] != key:
                    index = self.re_hashing(index)
                    if index == start:
                        raise Exception('fulled')
                
                if self.key[index] == None:
                    self.key[index] = key
                    self.data[index] = data
                else:
                    self.data[index] = data  # 替换值
        

    def get(self, key):
        index = self.hash_function(key)
        if self.key[index] == None:
            return None
        elif self.key[index] == key:
            return self.data[index]
        else:
            start = index
            index = self.re_hashing(index)
            while self.key[index] != None and self.key[index] != key:
                index = self.re_hashing(index)
                if index == start:
                    break
            if index == start:
                return None

            if self.key[index] == None:
                return None
            else:
                return self.data[index]

    def hash_function(self, key):
        return key%self.SZIE

    def re_hashing(self, index):
        return (index+1)%self.SZIE

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


a = HashTable()
a[11] = 'fsa'
a[31] = 'aa'
print(a[11])
print(a[31])
print(a[3])
print(a.data)