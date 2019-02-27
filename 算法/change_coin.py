"""
找零钱：
给出一定数额的钱，如何组合1，5，10，20，50面额的钱，使数量最少

解决思路：
使用递归, 找出一个最基本的情况
"""


def min_coins(coins, change):
    min_nums = change
    if change in coins:
        return 1
    else:
        for i in [c for c in coins if c<change]:
            nums = 1 + min_coins(coins, change-i)
            if nums < min_nums:
                min_nums = nums
    return min_nums

coins = [1,5,10,20]
print(min_coins(coins, 64))

"""
对递归的优化，使用缓存将已知的结果保存下来
"""
def min_coins2(coins, change, know_result):
    min_num = change
    if change in know_result:
        return know_result[change]
    elif change in coins:
        know_result[change]=1
        return 1
    else:
        for i in [c for c in coins if c<change]:
            nums = 1 + min_coins2(coins, change-i, know_result)
            if nums < min_num:
                min_num = nums
        know_result[change] = min_num
        return min_num

know_result = {}
print(min_coins2(coins,64, know_result))


"""
动态编程

思路：
从1计算到change，记录下每次需要换零钱的最小值
后面的值的计算会用到前面的结果
"""
def min_coins3(change):
    know_result = [0]*(change+1)
    coins = [1,5,10,20]
    for i in range(change+1):
        min_num = i # 初始化，最小的硬币数量是i个 
        for j in [c for c in coins if c<=i]:
            nums = know_result[i-j] + 1 # 遍历以前的结果，寻找最小的值
            if nums < min_num:
                min_num = nums
        know_result[i] = min_num
    
    print(know_result)

min_coins3(64)