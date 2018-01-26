'''
数组扁平化：
给出一个数组，数组里面还包含数组，给出一个单一的数组，如
[2,1,[3,[4,5],6,7],8,[9]] -----> [2,1,3,4,5,6,7,8,9]

解决思路：
使用递归解决
1. 遍历数组，判读它的元素是否为数组
2. 若是数组，则进行递归处理
3. 不是，则添加元素到单一数组，进行下一个元素处理
'''

a = [2,1,[3,[4,5],6,7],8,[9]]

def flatten(l,new_list=None):
    # 数组初始化
    new_list = list(new_list) if isinstance(new_list,(list,tuple)) else []

    for i in l:
        if isinstance(i,(list,tuple)):
            new_list = flatten(i,new_list)
        else:
            new_list.append(i)
    return new_list



new_list = flatten(a)
print(new_list)
