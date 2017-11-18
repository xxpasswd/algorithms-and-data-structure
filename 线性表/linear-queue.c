#include <stdio.h>
#include <stdlib.h>
#define ElementType int

//队列的链式存储实现

typedef struct node
{
	ElementType data;
	struct node *next;
}Qnode;

typedef struct
{
	Qnode *font;
	Qnode *rear;
}Queue;

Queue *Create()
{
	Queue *p;
	p=(Queue *)malloc(sizeof(Queue));
	p->font=NULL;
	p->rear=NULL;
	return p;
}

Queue *push(ElementType x,Queue *p)
{
	Qnode *temp;
	temp=(Qnode *)malloc(sizeof(Qnode));
	temp->data=x;
	temp->next=NULL;
	p->rear->next=temp;
	p->rear=temp;
	if(p->font==NULL) p->font=temp;
	return p;
}

ElementType pop(Queue *p)
{
	Qnode *temp;
	ElementType x;
	if(p->rear==NULL)
	{
		printf("Queue is empty\n");
		return NULL;
	}
	else
	{
		temp=p->font;
		p->font=temp->next;
		x=temp->data;
		free(temp);
		return x;
	}
}