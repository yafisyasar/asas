#include<stdio.h>
void main()
{
 int a[10],s=0,n,i;
 float avg;
 printf("enter no of elements:");
 scanf("%d",&n);
 printf("enter elements of array:");
 for(i=0;i<n;i++)
 {
  scanf("%d",&a[i]);
 }
 
 for(i=0;i<n;i++)
 {
  s=s+a[i];
 }
 avg=s/n;
 printf("avg of array elements:%0.1f",avg);
 }

