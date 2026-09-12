#include<stdio.h>
#include<stdlib.h>
int main()
{
int* p;
int s,i;
printf("enter size: ");
scanf("%d",&s);
p=(int*)calloc(s , sizeof(int));
if (p==NULL){
printf("allocation failed \n");
return 1;}
printf("Enter %d elements: \n",s);
for (i=0;i<s;i++){
scanf("%d",&p[i]);}
printf("elements are: ");
for (i=0;i<s;i++){
printf("%d ",p[i]);}
printf("\n");
free(p);
}