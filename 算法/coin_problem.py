'''
硬币问题
如何把一笔钱，组合出来

逆序编程，正序思考
'''

n = 0
def recMC(coinValueList,change,knowResult):
    global n
    n += 1
    minCoins = change
    if change in coinValueList:
        return 1
    elif knowResult[change] > 0:
        return knowResult[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList,change-i,knowResult)
            if numCoins < minCoins:
                minCoins = numCoins
                knowResult[change] = minCoins
    return minCoins


# print(recMC([1,5,10,25],63,[0]*64))
# print(n)

def rec_mc(coin_value_list,change):
    out = []
    coin_value_list.sort(reverse=True)
    find_solution(coin_value_list,change,0,'',out)
    return out

m = 0
def find_solution(coin_value_list,change,cur,path,out):
    global m
    m += 1
    if cur == change:
        # out.append(path)
        pass
    elif cur > change:
        return
    else:
        for i in [c for c in coin_value_list if c<= change-cur]:
            find_solution(coin_value_list,change,i+cur,path+','+str(i),out)
           
rec_mc([1,5,10,25],42)
print(m)