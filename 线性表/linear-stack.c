#include <stdio.h>
#include <stdlib.h>
#define ElementType int
#define MAX 20

//堆的顺序存储实现

typedef struct
{
	ElementType data[MAX];
	int top;
}Stack;

Stack *Create()
{
	Stack *p;
	p=(Stack *)malloc(sizeof(Stack));
	p->top=-1;
}

bool IsEmpty(Stack *p)
{
	if(p->top==-1) return true;
	else return false; 
}

void Push(ElementType x,Stack *p)
{
	if(p->top==MAX-1)
	{
		printf("Stack is full\n");
		return;
	}
	p->data[++(p->top)]=x;
	return;
}

ElementType pop(Stack *p)
{
	if(p->top==-1)
	{
		printf("Stack is empty\n");
		return NULL;
	}
	else return p->data[(p->top)--];
}	