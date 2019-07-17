"""
0-1背包问题，有n个物品，从这个n个物品中挑选出几个物品放进背包中，使这几个物品的数量最接近背包重量

解决思路1：
使用回溯思想，不满足的时候返回，继续下一次的寻找（代码实现的意思可参考八皇后问题）
goods是各个物品的重量
bag_weight是背包的最大重量
path是路径
cur是当前的重量
i是考察到哪个物品了

解决思路2：
使用动态规划
使用一个二维数组来保存前面的结果，后面的计算要依赖于前面的结果

如何打印出路线，使用了一个path，跟踪每次加的值

Date:2019-07-17
"""
goods = [9, 10, 4, 12, 6, 4, 3, 2, 7]
bag_weight = 49
trace = [None]*len(goods)
max_konw = 0
max_path = None

def solution(i, cur, path):
    global goods
    global bag_weight
    global max_konw
    global max_path
    if i == len(goods) or cur == bag_weight:
        if cur > max_konw:
            max_konw = cur
            max_path = path[:]
        return
    else:
        if cur + goods[i] <= bag_weight:
            path2 = path[:]
            path2[i] = goods[i]
            solution(i+1, cur+goods[i], path2)
        solution(i+1, cur, path[:])

solution(0, 0, trace)
print(max_konw)
print(max_path)


res = [[None]*(bag_weight+1) for i in range(len(goods)+1)]
res[0][0] = True

def soloution2(res, path):
    global goods
    global bag_weight
    for i in range(len(goods)):
        for j in range(bag_weight+1):
            if res[i][j] == True:
                res[i+1][j] = True
                path[i+1][j] = 0
                if j+goods[i] <= bag_weight:
                    res[i+1][j+goods[i]] = True
                    path[i+1][j+goods[i]] = goods[i]

    temp = res[len(goods)]
    for i in range(bag_weight, -1, -1):
        if temp[i] == True:
            return i

def print_path(path, start):
    out = []
    for i in range(len(goods), 0, -1):
        value = path[i][start]
        start = start - value
        out.append(value)
    print(out)


path = [[None]*(bag_weight+1) for i in range(len(goods)+1)]
r = soloution2(res, path)
print_path(path, r)

