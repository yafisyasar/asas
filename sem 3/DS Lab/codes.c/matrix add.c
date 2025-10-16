#include<stdio.h>
#include<stdlib.h>
void main()
{
int a[5][5],b[5][5],res[5][5];
int i,j;
printf("enter 1st metrix:");
for(i=0;i<2;i++)
{
 for(j=0;j<2;j++)
 {
  scanf("%d",&a[i][j]);
 }
}

printf("enter 2nd metrix:");
for(i=0;i<2;i++)
{
 for(j=0;j<2;j++)
 {
  scanf("%d",&b[i][j]);
 }
}

for(i=0;i<2;i++)
{
 for(j=0;j<2;j++)
 {
  res[i][j]=a[i][j]+b[i][j];
 }
}

printf("resultant metrix:\n");
for(i=0;i<2;i++)
{
 for(j=0;j<2;j++)
 {
  printf("%d ",res[i][j]);
 }
 printf("\n");
}

}
  
  
