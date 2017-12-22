#include <stdio.h>
#include <stdlib.h>
#define ElementType int

typedef struct
{	
	ElementType data;
	int length;
}List;

//顺序查找，时间复杂度O(n)
int SequentialSearch(List *p,ElementType x)
{
	int i;
	p->data[0]=x;//哨兵，假设原数组第一个位置没有存储数据
	for(i=p->length;p->data[i]!=x;i--);
	return i;//查找成功则返回下标，不成功则返回0
}

//二分查找，且假设原数组已按序存放,时间复杂度(logN)
int BinarySearch(List *p,ElementType x)
{
	int left,mid,right;
	left = 0;
	right = p->length;
	while(left<=right)
	{
		mid=(left+right)/2;
		if(x<p->data[mid]) right=mid-1;
		else if(x>p->data[mid]) left=mid+1;
		else return mid;
	}
	return NULL;
}