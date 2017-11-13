#include <stdio.h>
#include <stdlib.h>
#define MAX 10

typedef int ElementType;

void swap(int *a,int *b)
{
	int temp;
	temp = *a;
	*a = *b;
	*b = temp;
}
/*冒泡排序*/
void Bubble_Sort(ElementType a[],int N)
{
	ElementType tmp;
	for(int i=N-1;i>=0;i--)
	{
		for(int j=0;j<i;j++)
		{
			if(a[j]>a[j+1])
			{
				tmp = a[j];
				a[j] = a[j+1];
				a[j+1] = tmp;
			}
		}
	}
}

/*插入排序*/
void Insert_Sort(ElementType a[],int N)
{
	int i,j;
	ElementType tmp;
	for(i=1;i<N;i++)
	{
		tmp = a[i];
		for(j=i;j>0&&a[j-1]>tmp;j--)
		{
			a[j]=a[j-1];			
		}
		a[j]=tmp;
	}

}

/*希尔排序*/
void Shell_Sort(ElementType a[],int N)
{
	int i,j,d;
	ElementType tmp;
	for(d=N/2;d>0;d=d/2)
	{
		for(i=d;i<N;i++)
		{
			tmp=a[i];
			for(j=i;j>=d&&a[j-d]>tmp;j-=d)//从后往前比
				{
					a[j]=a[j-d];
				}
			a[j]=tmp;
		}
	}
}

void random_list(ElementType a[])
{
	for(int i=0;i<MAX;i++)
	{
		a[i] = (int)(rand()%100);
	}
}

/*归并算法,合并两个序列，f:序列1的长度，s：序列2的场长度*/
ElementType *two_merge(ElementType a[],ElementType b[],int f,int s)
{
	int t,i,j,k;
	i=j=k=0;// i,j,k分别为序列1，2，3的初始位置
	t=f+s-1;// 序列3的长度
	ElementType c[t];
	while(i<f&&j<s)
	{
		if(a[i]<b[j]) c[k++]=a[i++];
		else c[k++]=b[j++];
	}
	while(i<f) c[k++]=a[i++];
	while(j<s) c[k++]=b[j++]; 
	return c;
}

/*归并排序合并一个序列的两个部分 l：左边的初始位置，r右边的初始位置，e：右边的结束位置*/
void merge(ElementType a[],ElementType b[],int l,int r,int e)
{
	int lr=r-1;//左边序列的结束位置
	int tmp=l;//存放数组的初始位置
	int numelem = e-l+1;
	while(l<=lr&&r<=e)
	{
		if(a[l]<=a[r]) b[tmp++]=a[l++];
		else b[tmp++]=a[r++];
	}
	while(l<=lr) b[tmp++]=a[l++];
	while(r<=e) b[tmp++]=a[r++];
	for(int i=0;i<numelem;i++,e--)
		a[e]=b[e];
}

void merge_sort(ElementType a[],ElementType b[],int l,int r)//l:左边的位置，r:右边的位置
{
	int mid;
	if(l<r)
	{
		mid = (l+r)/2;
		merge_sort(a,b,l,mid);
		merge_sort(a,b,mid+1,r);
		merge(a,b,l,mid+1,r);
	}
}

//归并排序的统一接口
void M_sort(ElementType a[],int N)
{
	ElementType *tmp;
	tmp=(ElementType *)malloc(sizeof(ElementType)*N);
	merge_sort(a,tmp,0,N-1);
	free(tmp);
}

//归并排序的非递归实现
void merge_pass(ElementType a[],ElementType b[],int N,int length)//length:当前子序列的长度
{
	int i;
	for(i=0;i<=N-2*length;i+=2*length)
		merge(a,b,i,i+length,i+2*length-1);
	if(i+length<N) merge(a,b,i,i+length,N-1);
	else 
	{
		for(int j=i;j<N;j++)
			b[j]=a[j];
	}
}

void M_sort2(ElementType a[],int N)
{
	ElementType *tmp;
	int length=1;
	tmp=(ElementType *)malloc(sizeof(ElementType)*N);
	while(length<N)
	{
		merge_pass(a,tmp,N,length);
		length *=2;
	}
	free(tmp);
}

//快速排序
ElementType find_pivot(ElementType a[],int l,int r)//找主元,l:左边起始位置，r：结束位置
{
	int mid=(l+r)/2;
	if(a[l]>a[mid]) swap(&a[l],&a[mid]);
	if(a[l]>a[r]) swap(&a[l],&a[r]);
	if(a[mid]>a[r]) swap(&a[mid],&a[r]);
	swap(&a[mid],&a[r-1]);
	return a[r-1];
}

void Quicksort(ElementType a[],int l,int r)
{
	if((r-l)>1)
	{
		int i,j,pivot;
		pivot = find_pivot(a,l,r);
		i=l,j=r-1;
		for(;;)
		{
			while(a[++i]<pivot) {}
			while(a[--j]>pivot) {}
			if(i<j) swap(&a[i],&a[j]);
			else break;
		}
		swap(&a[i],&a[r-1]);
		Quicksort(a,l,i-1);
		Quicksort(a,i+1,r);
    }
    else
    {
    	if(a[l]>a[r]) swap(&a[l],&a[r]);
    }
}

void Quick_sort(ElementType a[],int N)
{
	Quicksort(a,0,N-1);
}

void show(ElementType a[])
{
	for(int i=0;i<MAX;i++)
		printf("%4d",a[i] );
}


int main(int argc, char const *argv[])
{
	int a[MAX];
	random_list(a);
	show(a);
	Quick_sort(a,MAX);
	printf("\n");
	show(a);

}