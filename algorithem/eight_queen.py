"""
八皇后问题:
在一个8x8的棋盘上，放置8个棋子，使8个棋子互相不在一条直线或者对角线上

解决思路：
使用回溯法，每次对下一个要放置的皇后进行判断，不满足条件，则移动上一个皇后的位置，继续判断
"""

# 说明：使用一个queue保存皇后的位置，数据的下标代表皇后的行，值代表列

BORDER_SIZE = 8
queen = [None] * 8

m = 0

def eight_queen(n):
    global m
    if n >= BORDER_SIZE:
        m += 1
        print(queen)

    for pos in range(BORDER_SIZE):
        if is_valid_pos(n, pos):
            queen[n] = pos
            eight_queen(n+1)


def is_valid_pos(n, pos):
    """
    判断两个皇后是否冲突
    1. 不在同一条列上
    2. 不在同一对角线上（两个点横纵坐标距离相等）
    """
    i = 0
    while i < n:
        if queen[i] == pos:
            return False
        if n-i == abs(pos-queen[i]):
            return False
        i += 1

    return True
    

eight_queen(0)
print(m)
