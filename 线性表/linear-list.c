#include <stdio.h>
#include <stdlb.h>
#define ElementType int
#define MAX 20

//线性表的顺序实现

typedef struct
{
	ElementType data[MAX];
	int last;
}List;

List *Create()
{
	List *p;
	p=(List *)malloc(sizeof(List));
	p->last=-1;
	return p;
}

bool IsEmpty(List *p)
{
	if(p->last==-1) return false;
	else return true;
}

ElementType FindKth(int k,List *p)
{
	if(p->last==-1)
	{
		printf("List is empty\n");
		return NULL;
	}
	if(k<1||k>p->last+1)
	{
		printf("wrong location\n");
		return NULL;
	}
	return p->data[k-1];
} 

int Find(ElementType x,List *p)
{
	int i=0;
	if(p->last==-1)
	{
		printf("List is empty\n");
		return NULL;
	}
	while(i<=p->last&&p->data[i]!=x) i++;
	if(i>p->last) return NULL;
	else return i;
}

void Insert(ElementType x,int k,List *p)
{
	int i;
	if(p->last==MAX-1)
	{
		printf("List is full\n");
		return;
	}
	if(k<1||k>p->last+2)
	{
		printf("Location is wrong\n");
		return NULL;
	}
	for(i=p->last;i>=k-1;i--) p->data[i+1]=p->data[i];
	p->last++;
	return;
}

ElementType Delete(int k,List *p)
{
	int i,temp;
	if(p->last==-1)
	{
		printf("List is empty\n");
		return;
	}
	if(k<1||k>p->last+1)
	{
		printf("Location is wrong\n");
		return NULL;
	}
	temp=p->data[k-1];
	for(i=k;i<=p->last;i--) p->data[i-1]=p->data[i];
	return temp;	
}