/* link-https://www.programiz.com/dsa/linked-list-operations   --insertion,deletion*/
#include<stdio.h>
#include<stdlib.h>
struct node
{
 int data;
 struct node *next;
};

void print(struct node *p)
{
 while(p!=NULL)
 {
  printf("%d \n",p->data);
  p=p->next;
 }
}

int main()
{
struct node *head;
struct node *a=NULL;
struct node *b=NULL;
struct node *c=NULL;

a=malloc(sizeof(struct node));
b=malloc(sizeof(struct node));
c=malloc(sizeof(struct node));

a->data=20;
b->data=45;
c->data=34;

a->next=b;
b->next=c;
c->next=NULL;

head=a;
print(head);
printf("deleting last element:\n");
struct node *p;
p=head;
while(p->next->next!=NULL)
{
 p=p->next;
}
 p->next=NULL;
print(head);


return 0;
}
