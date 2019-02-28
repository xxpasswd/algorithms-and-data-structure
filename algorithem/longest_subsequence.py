'''
给定一个序列，求出这个序列最长递增子序列

解决方法：
遍历序列，当前数的最长子序列就是前面所有小于此数中的最长子序列最大的一个加1
'''

def longest_subsequence(squence):
    # 存储每个位置上数的最长子序列的长度
    know_length = [1]*len(squence)
    # 存储每个位置上最长子序列
    path = ['']*len(squence)
    # 遍历每个数字
    for idx,num in enumerate(squence):
        # 假定最长子序列长度是1
        max_length = 1
        max_path = str(num)
        for i,pre_num in enumerate(squence[:idx]):
            # 当前面的数小于当前数，更新目前已知最长子序列长度
            if pre_num < num and max_length < know_length[i]+1:
                max_length = know_length[i]+1
                max_path = path[i] + '->' + str(num)
        know_length[idx] = max_length
        path[idx] = max_path    
    return max(know_length),max(path,key=lambda x:len(x.replace('->','')))
print(longest_subsequence([3,7,5,3,2,6,3,7,4,9,0,1,3,30,43,3,23,13,44,5]))