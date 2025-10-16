#include<stdio.h>
struct details
{
 int weight;
 int age;
 char gender[10];
}s1;
void main()
{
 struct details *ptr;
 ptr=&s1;
 printf("enter weight:");
 scanf("%d",&ptr->weight);
 printf("enter age:");
 scanf("%d",&ptr->age);
 printf("enter gender:");
 scanf("%s",ptr->gender);
 
 printf("\nage:%d\n",ptr->age);
 printf("weight:%d\n",ptr->weight);
 printf("gender:%s",ptr->gender);
}
