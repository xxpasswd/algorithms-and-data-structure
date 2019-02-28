#include <stdio.h>
#include <stdlib.h>
#define ElementType int

//堆栈的链式存储实现

typedef struct Node
{
	ElementType data;
	struct Node *next;
}Stack;

Stack *Create()
{
	Stack *p;
	p=(Stack *)malloc(sizeof(Stack));
	p->next=NULL;
	return p;
}

bool IsEmpty(Stack *p)
{
	if(p->next==NULL) return true;
	else return false;
}

void push(ElementType x,Stack *p)
{
	Stack *temp;
	temp=(Stack *)malloc(sizeof(Stack));
	temp->data=x;
	temp->next=p->next;
	p->next=temp;
}

ElementType pop(Stack *p)
{
	Stack *temp;
	ElementType x;
	if(p->next=NULL)
	{
		printf("stack is empty\n");
		return NULL;
	}
	temp=p->next;
	p->next=temp->next;
	x=temp->data;
	free(temp);
	return x;
}