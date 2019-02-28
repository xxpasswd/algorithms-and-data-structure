'''
给定一个数组和一个范围，求不在数组中的范围
example: [3,5] 1-10 ---> 1->2,4,6->10

解决思路：
遍历数组，和给定范围进行比较
'''

def get_missing_range(nums,left,right):
    
    # 存放输出结果
    out = []
    start = left
    for num in nums:
        if start < num <= right:
            out.append(get_range(start,num-1))
            start = num+1
        elif num == start:
            start += 1
            
    if start <= right:
        out.append(get_range(start,right))
    return out


def get_range(n1,n2):
    if n1 == n2:
        return n1
    else:
        return str(n1) + '->' + str(n2)


nums = [3, 5, 10, 11, 12, 15, 19]
print(get_missing_range(nums,1,20))


# def missing_ranges(nums, lo, hi):
#     res = []
#     start = lo
#     for num in nums:
#         if num < start:
#             continue
#         if num == start:
#             start += 1
#             continue
#         res.append(get_range(start, num-1))
#         start = num + 1
#     if start <= hi:
#         res.append(get_range(start, hi))
#     return res

# def get_range(n1, n2):
#     if n1 == n2:
#         return str(n1)
#     else:
#         return str(n1) + "->" + str(n2)

# nums = [3, 5, 10, 11, 12, 15, 19]
# print("original:", nums)
# print("missing range: ", missing_ranges(nums,0,20))
