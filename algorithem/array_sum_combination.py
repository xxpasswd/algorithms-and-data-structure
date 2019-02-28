'''
给出三个数组，从三个数组中各取一个数，使这个三个数加起来等于特定值

'''

A = [1, 2, 3, 3]
B = [2, 3, 3, 4]
C = [1, 2, 2, 2]
target = 7

def array_sum_combination(l1:list,l2:list,l3:list,target:int)->list:
    out = set()
    for i in l1:
        for j in l2:
            for k in l3:
                if i + j + k == target:
                    out.add((i,j,k))
    
    return out


# python里面有更好的工具实现多重循环
import itertools
from functools import partial

def check_sum(N, *nums):
    if sum(x for x in nums) == N:
        return (True, nums)
    else:
        return (False, nums)

pro = itertools.product(A,B,C)
func = partial(check_sum, target)
sums = list(itertools.starmap(func, pro))

res = set()
for s in sums:
    if s[0] == True and s[1] not in res:
        res.add(s[1])
print(res)

print(array_sum_combination(A,B,C,target))