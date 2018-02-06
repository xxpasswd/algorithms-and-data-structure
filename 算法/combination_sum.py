'''
给定一个数组和一个数T，找出在数组中，所有可能等于T的数的组合，数组中的数可以重复使用

解决思路：
使用深度优先遍历
从一个数开始进行，记下它经过的节点，若不满足，则返回上一节点，继续进行
'''

def combination_sum(candidates,target):
    res = []
    candidates.sort()
    dfs(target,candidates,0,[],res)
    return res

def dfs(target,candidates,index,path,res):
    '''
    target:目标数
    candidates:候选数组
    index:开始遍历的索引
    path：经过的路径
    res：保存结果的数组，发现满足条件的路径时进行保存
    '''
    
    # 先判断此次遍历是否满足条件，不满足条件时，直接回溯
    if target < 0:
        return  # 回溯
    elif target == 0:
        res.append(path)
        return
    # 继续遍历
    else:
        for i in range(index,len(candidates)):
            # 此处path不能用append方法，append方法不会返回值，因此没有path的值会传递下去
            dfs(target-candidates[i],candidates,i,path+[candidates[i]],res) 

print(combination_sum([2,3,6,7],7))