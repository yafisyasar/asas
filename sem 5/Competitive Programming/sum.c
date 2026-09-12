#include<stdio.h>
#include<stdlib.h>
int main()
{
int* p;
int s,i,a=0;
printf("enter size: ");
scanf("%d",&s);
p=(int*)calloc(s , sizeof(int));
if (p==NULL){
printf("allocation failed \n");
return 1;}
printf("Enter %d elements: \n",s);
for (i=0;i<s;i++){
scanf("%d",&p[i]);}
for (i=0;i<s;i++){
a+=p[i];}
printf("sum: %d",a);
printf("\n");
free(p);
}