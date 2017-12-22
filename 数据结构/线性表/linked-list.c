#include <stdio.h>
#include <stdlib.h>
#define ElementType int

//线性表的链式存储实现

typedef struct node
{
	ElementType data;
	struct node *next;
}List;

List *Create()
{
	List *p;
	p=(List	*)malloc(sizeof(List));
	p->next=NULL;
	return p;
}

int Length(List *p)
{
	int i=0;
	List *temp=p;
	while(temp->next!=NULL)
	{
		temp=temp->next;
		i++;
	}	
	return i;
}

//按值查找
List *Find(ElementType x,List *p)
{
	List *temp=p;
	while(temp!=NULL&&temp->data!=x)
	{
		temp=temp->next;
	}
	return temp;

}

//按序号查找
List *FindKth(int k,List *p)
{
	int i=1;
	List *temp=p;
	while(temp!=NULL&&i<k)
	{
		temp=temp->next;
		i++;
	}
	if(i==k) return temp;
	else return NULL;
}

List Insert(ElementType x,int k,List *p)
{
	List *s,*temp;
	if(k=1)
	{
		s=(List *)malloc(sizeof(List));
		s->data=x;
		s->next=p;
		p=s;
		return p;
	}
	temp=FindKth(k-1,p);
	if(!temp)
	{
		printf("location is wrong\n");
		return p;	
	} 
	else
	{
		s=(List *)malloc(sizeof(List));
		s->data=x;
		s->next=temp->next;
		temp->next=s;
		return p;	
	}
}

List *Delete(int k,List *p)
{
	List *s,*temp;
	int i=1;
	if(k==1)
	{
		temp=p;
		if(p=!NULL) p=p->next;
		free(temp);
		return p;
	}
	s=FindKth(k-1,p);
	if(!s)
	{
		printf("Location is wrong\n");
		return p;
	}
	else if(p->next==NULL)
	{
		printf("Location is wrong\n");
		return p;
	}
	else
	{
		temp=s->next;
		s->next=temp->next;
		free(temp);
		return p;
	}
}