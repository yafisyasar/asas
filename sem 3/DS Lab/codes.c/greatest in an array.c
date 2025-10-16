#include<stdio.h>
#include<stdlib.h>
void main()
{
 int a[10],i,j,n,grt;
 printf("enter array size:");
 scanf("%d",&n);
 printf("enter elements:");
 for(i=0;i<n;i++)
 {
  scanf("%d",&a[i]);
 }
  for(i=0;i<n;i++)
  {
   for(j=0;j<n;j++)
   {
    if(a[j]>a[i])
    {
     grt=a[j];
    }
   }
  }
  printf("greatest element= %d",grt);
 }
