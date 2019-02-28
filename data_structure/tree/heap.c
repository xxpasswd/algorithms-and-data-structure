#include <stdio.h>
#include <stdlib.h>
#define ElementType int
#define MAX 20
#define MaxData 100000

typedef struct
{
	ElementType *data;
	int size;
	int capacity;
}MaxHeap;

MaxHeap *Create(int MAX)
{
	MaxHeap *p;
	p =(MaxHeap *)malloc(sizeof(MaxHeap));
	p->data = (ElementType *)malloc((MAX+1)*sizeof(ElementType));
	p->size = -1;
	p->capacity = MAX;
	p->data[0] = MaxData;
}

void Insert(ElementType x,MaxHeap *p)
{
	if(p->size==p->capacity)
	{
		printf("Heap is full!\n");
		return;
	}
	p->size++;
	p->data[p->size]=x;
	int parent = (p->size)/2;
	int now_node = p->size;
	while(x>p->data[parent])
	{	
		now_node = parent;
		p->data[p->size] = p->data[parent];
		parent = parent/2;
	}
	p->data[now_node] = x;
}

ElementType Delete(MaxHeap *p)
{
	ElementType MaxIterm,temp;
	int child,parent;
	if(p->size==-1)
	{
		printf("Heap is empty!\n");
		return NULL;
	}
	MaxIterm = p->data[1];
	temp = p->data[(p->size)--];
	for(parent=1,child=2;parent*2<=p->size;parent=child)
	{
		child = parent*2;
		if(child!=p->size&&p->data[child]<p->data[child+1])
		{
			child++;
		}
		if(temp<p->data[child])
		{
			p->data[parent] = p->data[child];
		}
		else break;
	}
	p->[parent] = temp;
	return MaxIterm;
}