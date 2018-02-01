'''
求一个字符的全排列

解决思路：
使用递归
'''


def inner_all_perms(elements):
    # 当只剩最后一个元素时，返回
    if len(elements) == 1:
        return elements


