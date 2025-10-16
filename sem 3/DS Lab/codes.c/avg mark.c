#include<stdio.h>
void main()
{
 int a[10],n,s=0;
 float avg;
 printf("enter limit:");
 scanf("%d",&n);
 for(int i=1;i<=n;i++)
 {
  printf("enter mark %d:",i);
  scanf("%d",&a[i]);
  s=s+a[i];
 }
avg=s/n;
printf("avg=%0.2f",avg);
} 

