'''
给定一个数组s和一个数t，在数组中寻找两个数a、b，使a+b=t,找出一组满足条件的a，b

解决思路：
遍历数组，每遇到一个数，记下该数需要满足条件的另一个数，若在接下来的遍历中，遇到了这个数，则返回这组数
'''


def two_sum(nums:"List[int]", target:"int")->"List[int]":
    dic = {}
    for i, num in enumerate(nums):
        if num in dic:
            return [dic[num], i]
        else:
            dic[target - num] = i


if __name__ == "__main__":
    arr = [1,2,4,5]
    target = 6
    res = two_sum(arr, target)
    print(res)