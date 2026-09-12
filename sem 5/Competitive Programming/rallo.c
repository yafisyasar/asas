#include<stdio.h>
#include<stdlib.h>
int main()
{
int* p;
int s;
printf("enter size: ");
scanf("%d",&s);
p=(int*)calloc(s , sizeof(int));
if (p==NULL){
printf("allocation failed \n");}
else{
printf("allocated successfully \n");
for(int j=0;j<s;++j){
p[j]=j+1;}
printf("elements are: ");
for(int k=0;k<s;++k){
printf("%d ",p[k]);}
printf("\n");
s=10;
int *temp=p;
p=realloc(p,s*sizeof(int));
if (p==NULL){
printf("re-allocation failed \n");
p=temp;}
else{
    printf("re-allocated successfully \n");
}
for(int j=5;j<s;++j){
p[j]=j+1;}
printf("elements are: ");
for(int k=0;k<s;++k){
printf("%d ",p[k]);}
printf("\n");
}
}