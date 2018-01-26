"""
数组重排，奇数在前，偶数在后

思路：
类似冒泡排序，和后面的数比较，若是偶数，就交换位置
"""

array = [1,2,4,5,6,7,9,0]

count = len(array)

for i in range(count-1):
    for j in range(i+1,count):
        if array[i]%2==0 and array[j]%2==1:
            array[i],array[j] =array[j],array[i]

print(array)
