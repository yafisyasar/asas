#include<stdio.h>
#include<stdlib.h>
void main()
{
 int a[5][5],b[5][5],res[5][5];
 int i,j,k,r,c;
 printf("enter row size:");
 scanf("%d",&r);
 printf("enter col size:");
 scanf("%d",&c);
 
 printf("enter 1st matrix:");
 for(i=0;i<r;i++)
 { 
  for(j=0;j<c;j++)
  {
  scanf("%d",&a[i][j]);
  }
 }
 
 printf("enter 2nd metrix:");
 for(i=0;i<r;i++)
 {
  for(j=0;j<r;j++)
   {
    scanf("%d",&b[i][j]);
   }
  }
  
  for(i=0;i<r;i++)
  {
   for(j=0;j<c;j++)
   {
    res[i][j]=0;
   }
  }
  
 for(i=0;i<r;i++)
 {
  for(j=0;j<c;j++)
  {
   for(k=0;k<r;k++)
   {
    res[i][j]=res[i][j]+(a[i][k]*b[k][j]);
   }
  }
 }
 
 printf("resultant metrix:\n");
 for(i=0;i<r;i++)
 {
  for(j=0;j<r;j++)
  {
   printf("%d ",res[i][j]);
  }
  printf("\n");
 }
 
}
