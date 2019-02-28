'''
给定一个整数，求出这个数所有可能的因子乘积，因子必须大于1

解决思路：
对于每一个因子，逐步分解
'''

# 迭代
def getFactors(n):
    # todo，后续要分解的数，n，当前要分解的数，2，当前开始的分解因子，[],分解数前面的因子 
    todo, combis = [(n, 2, [])], []
    while todo:
        n,i,combi = todo.pop()
        while i*i <= n:
            if n % i == 0:
                combis.append(combi + [i,n//i])
                todo.append((n//i,i,combi + [i]))
            i += 1
    return combis        

print(getFactors(36))

# 递归
def getFactors2(n):
    def factor(n,i,combi,combis):
        '''
        n：当前要分解的数
        i：当前的因子的开始数
        combi：前面已分解的因子集合
        combis:最终因子分解的集合
        '''

        while i*i <= n:
            if n % i == 0:
                combis.append(combi + [i,n//i])
                factor(n//i,i,combi + [i],combis)
            i += 1
        return combis
    return factor(n,2,[],[])

print(getFactors2(36))
                
