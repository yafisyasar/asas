#include<stdio.h>
#include<stdlib.h>
void main()
{
int i,j,t,a[10],n;
printf("enter array size:");
scanf("%d",&n);  
printf("enter elements:");
for(i=0;i<n;i++)
{
 scanf("%d",&a[i]);
}

for(i=0;i<n;i++)
{
 for(j=0;j<n-1;j++)
 {
  if(a[j]>a[j+1])
  {
   t=a[j];
   a[j]=a[j+1];
   a[j+1]=t;
   }
  }
 }

printf("elements:\n");
for(i=0;i<n;i++)
{
 printf("%d\n",a[i]);
}
}                                    
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                                      
                       
