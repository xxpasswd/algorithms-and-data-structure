'''
给定几个间隔集合，合并所有的重叠间隔

解决思路：
1. 若两个间隔有重叠的部分，则求并集
2. 若两个间隔没有重叠的部分，则是两个独立的间隔
'''


# 定义一个间隔类，表示间隔
class Interval(object):
    def __init__(self,start,end):
        self.start = start
        self.end = end

def merge_interval(interval_list):
    # 最后输出的间隔列表
    out = []
    
    for interval in sorted(interval_list,key=lambda i:i.start):
        if out and interval.start <= out[-1].end:
            out[-1].end = max(interval.end,out[-1].end)
        # 若没有重叠的时候
        else:
            out.append(interval)

    return out


if __name__ == '__main__':
    given = [[1,4],[2,7],[8,10],[12,17],[13,15]]
    interval_list = []
    for l,r in given:
        interval_list.append(Interval(l,r))

    print([(x.start,x.end) for x in merge_interval(interval_list)])
