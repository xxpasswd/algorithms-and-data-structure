'''
给定一组数字，给这组数字中，添加+，-，*，使最后表达式的结果等于特定值

解决思路：
使用递归遍历所有的情况
'''

def expression_add_operators(nums,target):
    out = []
    helper(nums,target,0,0,0,'',out)
    return out

def helper(nums,target,pos,pre,pre_num,path,out):
    '''
    nums:候选数字
    target：目标值
    pos：下一个数字开始的索引
    pre：前一次计算的值
    pre_num：前一个数字
    path：已经过的运算路径
    out：保存输出结果的列表
    '''

    # 判断路径的结果，是否满足条件，满足条件则添加到结果集中
    if pos == len(nums):
        if pre == target:
            out.append(path)
        return
    elif pos == 0:
        # 注意i+1这儿
        for i in range(pos,len(nums)):
            cur = int(nums[pos:i+1])
            helper(nums,target,i+1,cur,cur,path + str(cur),out)
    else:
        for i in range(pos,len(nums)):
            cur = int(nums[pos:i+1])
            helper(nums,target,i+1,pre+cur,cur,path + '+' + str(cur),out)
            helper(nums,target,i+1,pre-cur,-cur,path + '-' + str(cur),out)
            helper(nums,target,i+1,pre-pre_num+pre_num*cur,pre_num*cur,path + '*' + str(cur),out)

nums = '123456'
target = 0
print(expression_add_operators(nums,target))