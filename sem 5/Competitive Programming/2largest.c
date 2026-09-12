#include<stdio.h>
#include<stdlib.h>
int main()
{
int* p;
int s,i,l=0,temp;
printf("enter size: ");
scanf("%d",&s);
p=(int*)malloc(s * sizeof(int));
if (p==NULL){
printf("allocation failed \n");
return 1;}
printf("Enter %d elements: \n",s);
for (i=0;i<s;i++){
scanf("%d",&p[i]);}
for (i=0;i<s;i++){
if(l<p[i]){
    temp=l;
    l=p[i];
    p[i]=temp;
}
}
printf("second largest: %d",p[i-1]);
printf("\n");
free(p);
}