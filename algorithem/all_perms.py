'''
求一个字符的全排列

解决思路：使用递归
当有一个字符时，这个字符即为全排列
当有两个字符时，两个字符互相交换下位置，总共有两种
当有三个字符时，先选出一个字符，和剩下两个组合
当有四个字符时，先选出一个字符，和剩下三个组合


具体实现，反向递归：
    假设你已经知道求n-1个元素的全排列perms(n-1)
    则求n个元素，就是遍历这n个元素中的每一个i，则结果就是'i+perms(n-1)'

'''


# 反向递归
def all_perms(elements:str)->"单个元素时str，多个元素时list":
    # 只有一个元素时，就直接返回结果
    if len(elements) == 1:
        return elements
    # 多余一个元素时，进行递归
    else:
        out = []
        for i,j in enumerate(elements):
            # 和perms(n-1)里的每一个元素组合
            for k in  all_perms(elements[:i]+elements[i+1:]):
                temp = j+k
                out.append(temp)
    return out



words = 'abc'
print(all_perms(words))
