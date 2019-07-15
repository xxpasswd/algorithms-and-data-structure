"""
求一个数组的逆序度

解决思路：
分而治之，借助归并排序
"""

nums = 0
def reverse_pairs(alist):
    global nums
    merge_sort(alist)
    return nums

def merge_sort(alist):
    global nums
    if len(alist) <= 1:
        return alist
    else: 
        mid = len(alist) // 2
        left = merge_sort(alist[:mid])
        right = merge_sort(alist[mid:])
        res = []
        l, r = 0, 0 
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                l += 1
            else:
                r += 1
                nums += len(left) - l

        while left and right:
            if left[0] <= right[0]:
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))
        return res + left + right


if __name__ == "__main__":
    print(reverse_pairs([2,4,3,1,5,6]))
