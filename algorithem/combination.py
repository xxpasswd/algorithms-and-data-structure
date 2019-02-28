'''
求一个数组的组合

解决思路：
使用递归
'''

# 还未完成
# def combination(nums,n):
#     nums = list(nums)
#     # 当给定组合的数目大于数组长度时，返回全部数组
#     if n > len(nums):
#         return nums

#     def comb_helper(nums,n):
#         if n == 1:
#             for i in nums:
#                 return i



# 求全排列
def permutations(nums):
    if len(nums) == 1:
        yield nums
    else:
        for i,s in enumerate(nums):
            for k in permutations(nums[:i]+nums[i+1:]):
                temp = s + k
                yield temp


