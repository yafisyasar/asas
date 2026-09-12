#include<stdio.h>
#include<stdlib.h>
void main()
{
int* p;
int s;
printf("enter size: ");
scanf("%d",&s);
p=(int*)malloc(s * sizeof(int));
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
}
}
