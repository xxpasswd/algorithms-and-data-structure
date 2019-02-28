'''
给定一个数组s，在数组中选取3个数a、b、c，使a+b+c=0

解决办法：
1.数组排序，先取a的值，b初始时取a后面的数，c初始时取最后一个数
2.计算a+b+c的值，若小于0，则右移b，若大于0，则左移c，直到发现满足条件的值
3.进行下一轮遍历，更新a的值
'''

def three_sum(nums:"List[int]")->"List[int]":
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        # 若此次和上次的值相同，则去掉
        if nums[i] == nums[i-1]:
            continue
        # 初始化a、b、c的值，b初始时取a后面的数，c初始时取最后一个数
        a = i
        b = i+1
        c = len(nums)-1
        # 当b和c相遇时停止循环
        while b < c:
            s = nums[a]+nums[b]+nums[c]
            if s < 0:
                b += 1
            elif s > 0:
                c -= 1
            else:
                res.append((nums[a],nums[b],nums[c]))
                # 更新b，c
                # 去掉重复的值
                if nums[b] == nums[b+1]:
                    b += 1
                if nums[c] == nums[c-1]:
                    c -= 1
                b += 1
                c -= 1
    return res
        


if __name__ == "__main__":
    x = [-1,0,1,2,-1,-4]
    print(three_sum(x))