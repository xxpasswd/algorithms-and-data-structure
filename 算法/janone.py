'''
报数问题：
有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子

解决思路：
使用循环，当没有人时停止
'''

a = [1,2,3,4,5,6,7,8,9,10]


def circular_pop(people_list,skip):
        
        # 从下标为0的地方开始
        idx = 0 
        lenth = len(people_list)
        # 当长度小于0时，停止循环
        while lenth > 0:
            # 计算下一个要退的人，-1是因为从当前idx报数，当前idx不应算在里面
            idx = (idx+skip-1)%lenth
            print(people_list.pop(idx),end=' ')
            lenth -= 1
            

circular_pop(a,3)