"""
快速排序 O(nlogn) <----> O(n^2)

介绍：
选出一个枢纽值，然后，从数组的左右两边开始，依次从左边找到一个大于枢纽值的值，从右边找到一个小于枢纽值的值，
交换两个值的位置，直到左右两边找值的时候碰头，这时候，碰头的位置，应该是枢纽值的位置

编写思路（递归）
    基本用例，数组长度为1的时候，不需要处理了
"""

def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist)-1)

def quick_sort_helper(alist, start, end):
    if start < end:
        left = start + 1
        right = end
        pivot = start
        done = False
        while not done:
            while left <= right and alist[left] <= alist[pivot]:
                left += 1
            while left <= right and alist[right] >= alist[pivot]:
                right -= 1
            if right < left:
                done = True
            else:
                alist[left], alist[right] = alist[right], alist[left]
        alist[pivot], alist[right] = alist[right], alist[pivot]

        quick_sort_helper(alist, 0, right)
        quick_sort_helper(alist, right+1, end)


alist = [54,26,93,17,77,31,44,55,20]
quick_sort(alist)
print(alist)
            