"""
归并排序 O(nlogn)

程序编写思路（递归）：

基本用例
    1. 数组长度等于1
    2. 数组长度等于2
递归调用：
    数组长度大于3时，将数组分为左右两半，左右两半排序完后，将左右两半合并

"""
def merge_sort(alist):
    if len(alist) == 1:
        return alist
    elif len(alist) == 2:
        if alist[0] > alist[1]:
            alist[0], alist[1] = alist[1], alist[0]
        return alist
    else:
        mid = len(alist) // 2
        print('merger:', alist)
        left = merge_sort(alist[:mid])
        right = merge_sort(alist[mid:])
        
        i = 0
        j = 0
        k = 0
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            alist[k] = left[i]
            k += 1
            i += 1

        while j < len(right):
            alist[k] = right[j]
            k += 1
            j += 1

        return alist



def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
# mergeSort(alist)
# print(alist)
print(merge_sort(alist))

    