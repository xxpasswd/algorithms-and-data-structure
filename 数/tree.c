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


//二叉搜索树
Tree *Find(ElementType x,Tree *temp)
{
	if(!temp) return NULL;
	if(x<temp->data) return Find(x,temp->left);
	else if(x>temp->data) return Find(x,temp_right);
	else return temp;
}

Tree *Find2(ElementType x,Tree *temp)
{
	while(!temp)
	{
		if(x<temp->data) temp=temp->left;
		else if(x>temp->data) temp=temp->right;
		else return temp;
	}
	return NULL;
}

Tree *FindMin(Tree *temp)
{
	if(!temp) return NULL;
	if(!temp->left) return temp;
	else FindMin(temp->left);
}

Tree *FindMax(Tree *temp)
{
	if(!temp) return NULL;
	while(temp->right)
		temp=temp->right;
	return temp;
}

void Insert(ElementType x,Tree *p)
{
	if(!p)
	{
		Tree *temp;
		temp=(Tree *)malloc(sizeof(Tree));
		temp->data=x;
		temp->left=NULL;
		temp->right=NULL;
		return temp;
	}
	else if(x<p->data) p->left=Insert(x,p->left);
	else if(x>p->data) p->right=Insert(x,p->right);
}

void Delete(ElementType x,Tree *p)
{
	Tree *temp,*temp2;
	if(!p) printf("location wrong\n");
	else if(x<p->data) p->left=Delete(x,p->left);
	else if(x>p->data) p->left=Delete(x,p->right);
	else
	{
		if(p->left&&p->right){
			temp = Findmin(p->right);
			p->data = temp->data;
			p->right=Delete(p->data,p->right);
		}
		else
		{	
			temp = p;
			if(!p->left) p = p->right;
			else if(!p->right) p=p->left;
			free(temp);
		}
	}
}