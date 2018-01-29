'''
把一个数组旋转k步
example：[1,2,3,4,5,6] k=2 ----> [5,6,1,2,3,4]
'''

def rotate_array(nums,k):
    for i in range(k):
        temp = nums.pop()
        nums.insert(0,temp)

    return nums

def rotate_array2(nums,k):
    new_nums = []
    length = len(nums)
    for i in range(length):
        new_nums.append(nums[(length-k+i)%length])
    
    return new_nums

nums = [1,2,3,4,5,6]
# print(rotate_array(nums,2))
print(rotate_array2(nums,2))