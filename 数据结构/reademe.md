# python 内部数据结构的效率

## 列表

Operation|Big-O Efficiency
-----|-----
index|O(1)
index assignment|O(1)
append(item)|O(1)
insert(i,item)|O(n)
pop()|O(1)
pop(i)|O(n)
get slice|O(k)
set slice|O(n+k)
del slice|O(n)
concatenate|O(n)
contain|O(n)
sort()|O(nlogn)
reverser()|O(n)
del operator|O(n)
iteration|O(n)

## 字典

操作|效率
-----|------
copy|O(n)
get(item)|O(1)
set(item)|O(1)
delete item|O(1)
contain|O(1)
iteration|O(n)
