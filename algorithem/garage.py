
'''
车库问题：
有一个空位0，其他的都为车，所有的车每次交换位置时，必须通过空位进行交换，调到特定状态时的最少位数
如[1,2,0] 变为 [2,0,1] 需进行两步：第一步：[0,2,1] 第二步：[2,0,1]

解决思路：
现将所有能够和空位交换一次就能到达最终状态的车进行交换，直到初始空位位置和最终状态的空位位置相同时，   
剩下的，无法在通过一次交换就能满足最终状态，必须和空位进行两次交换，才能到达相应的状态
    第一步：将需要交换的位置的错误车辆和空位交换，
    第二步：将空位和正确的车辆交换

具体算法：
先判断两个状态的空位0是否相同
    若不相同：则先把初始位置空位0的车辆交换为最终需要停放的车
    若相同：则对比两个状态的每一个位置，找到不相同的位置，现将此位置空出来，即此位置和空位进行交换，再进行第一步

'''

def garage(initial, final):
    step = 0
    # 空位的初始位置
    while initial != final:
        zero = initial.index(0)
        # 判断开始，最终状态空位是否相同
        if zero != final.index(0):
            # 空位应该放的车
            car_to_move = final[zero]
            # 车的具体位置
            pos = initial.index(car_to_move)
            # 交换车和空位
            initial[zero],initial[pos] = initial[pos],initial[zero]
        else:
            for i,_ in enumerate(initial):
                if initial[i] != final[i]:
                    initial[zero],initial[i] = initial[i],initial[zero]
                    break
        step += 1
        print(initial)
    return step


if __name__ == "__main__":
    initial = [1, 2, 3, 0, 4]
    final = [0, 3, 2, 1, 4]
    print("initial:", initial)
    print("final:", final)
    print(garage(initial, final))
