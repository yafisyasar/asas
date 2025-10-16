#include<stdio.h>
void main()
{
 int n,i;
 int arr[]={23,56,7,56,78};
 n=5;
 int *ptr=arr;
 int *max=arr;
 int *min=arr;
 for(i=1;i<n;i++)
 {
  if(*(ptr+i)>*max)
  {
   max=ptr+i;
  }
   if(*(ptr+i)<*min)
   {
    min=ptr+i;
   }
  }
  
  printf("greatest=%d\n",*max);
  printf("smallest=%d",*min);
 }
 
