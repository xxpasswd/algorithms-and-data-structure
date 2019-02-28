"""
给出一个候选数字的集合C和目标数字T，找出集合C中任意的任意组合，只要满足组合的数字加起来等于T

思路：
使用动态规划
首先对集合C进行去重排序
遍历集合C中的数m，若m小于T，则令T=T-m，将m计入组合，继续循环遍历
若m>T，则停止这层遍历，返回上层遍历
若m=T，则输出这一组合
"""

C = [4,2,3,6,7]
T = 10
l = []
L = []


C =sorted(list(set(C)))
def search_num(C,T,l):
    l = list(l)
    for n,m in enumerate(C):
        if m<T:
            C=C[n:]
            #提前判断下下次循环能否进行
            if next_cycle(C,T,m):
                l.append(m)
                search_num(C,T-m,l)
                l.remove(m)
            else:
                continue
        elif m == T:
            l.append(m)
            L.append(list(l))
            break
        else:
            continue

# 当前T的值减去减去m能否大于下次C中的值
def next_cycle(C,T,m):
    for k in C:
        if k <= T - m:
            return True
    else:
        return False

search_num(C,T,l)

print(L)
