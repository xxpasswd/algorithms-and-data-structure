#include <stdio.h>
#include <stdlib.h>
#define ElementType int

typedef struct Node
{
	ElementType data;
	struct Node *left;
	struct Node *right;
}Tree;

Tree *Create()
{
	Tree *p;
	p=(Tree *)malloc(sizeof(Tree));
	p->left=NULL;
	p->right=NULL;
	return p;
}

//递归先序遍历
void PreOrderTravel(Tree *p)
{
	if(p)
	{	
		printf("%d\n",p->data);
		PreOrderTravel(p->left);
		PreOrderTravel(p->right);
	}
}


/*
	堆函数：
	Stack *CreateStack():创建一个空堆
	bool IsEmpty(Stack *s):判断堆是否为空
	void push(Tree *p,Stack *s):入堆
	Tree *pop(Stack *s):出堆
*/
//非递归中序遍历
void InorderTravel(Tree *p)
{
	Tree *temp=p;
	Stack *s;
	s = CreateStack();
	while(temp||!IsEmpty(s))
	{
		while(temp){
			push(temp,s);
			temp=temp->left;
		}
		if(!IsEmpty(s))
		{
			temp = pop(s);
			printf("%d\n",temp->data);
			temp=temp->right;
		}
	}
}

/*
	队列函数：
	Queue *CreateQueue():创建一个空队列
	bool IsEmpty(Queue *s):判断队列是否为空
	void push(Tree *p,Queue *s):入队列
	Tree *pop(Queue *s):出队列
*/
//层序遍历
void LevelTravel(Tree *p)
{
	Tree *temp=p;
	Queue *q;
	q = CreateQueue();
	pop(temp,q);
	while(temp||!IsEmpty(q))
	{
		temp=pop(q);
		printf("%d\n",temp->data );
		if(temp->left) push(temp->left,q);
		if(temp->right) push(temp->right,q);
	}
}
