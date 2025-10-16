#include<stdio.h>
struct student
{
 int id;
 char name[20];
};
void main()
{
struct student s1={121,"mike"};
struct student *ptr=&s1;
printf("name and id: %s %d",ptr->name,ptr->id);
}

