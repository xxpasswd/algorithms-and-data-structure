'''
给定一个排过序的数组，给出它的范围总结
example：[1,2,3,6,7,8,10] ----> ["1->3","6->8","10"]
'''

def summary_ranges(nums):
    # 开始的左端点
    start = nums[0]
    # 范围结束右端点，初始化为数组第一个数
    last = nums[0]
    # 输出结果
    out_list = []

    for i in nums[1:]:
        # 当数字连续时，更新右端点
        if i == last + 1:
            last = i
        # 当连续出现断裂时，更新开始节点
        else:
            out_list.append(get_range(start,last))
            start = i
            last = i
    else:
        out_list.append(get_range(start,last))
    
    return out_list

def get_range(start,last):
    if start == last:
        return str(start)
    else:
        return str(start) + '->' + str(last)


nums = [1,2,3,6,7,8,10]
print(summary_ranges(nums))
    