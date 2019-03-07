#include <stdio.h>
#include <stdlib.h>
#define ElementType int
#define MAX 20

//队列的顺序存储实现（循环队列）

typedef struct
{
	ElementType data[MAX];
	int font;
	int rear;
}Queue;

Queue *Create()
{
	Queue *p;
	p=(Queue *)malloc(sizeof(Queue));
	p->font=-1;
	p->rear=-1;
	return p;
}

bool IsFull(Queue *p)
{
	if(p->font=(p->rear+1)%MAX) return true;
	else return false;
}

bool IsEmpty(Queue *p)
{
	if(p->font==p->rear&&p->font!=-1) return true;
	else return false;
}

void push(ElementType x,Queue *p)
{
	if(IsFull) 
	{
		printf("Queue is IsFull\n");
		return;
	}
	else
	{
		data[(p->rear+1)%MAX]=x;
		p->rear++;
	}
}

ElementType pop(Queue *p)
{
	if(IsEm
		pty) 
	{
		printf("Queue is empty\n");
		return;
	}
	else
	{
		return p->data[p->font++];
	}
}