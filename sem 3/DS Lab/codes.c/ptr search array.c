  #include<stdio.h>
void main()
{
 int i,a[10],key,f=0,n;
 int *ptr;
 printf("enter array size:");
 scanf("%d",&n);
 printf("enter elements:");
 for(i=0;i<n;i++)
 {
  scanf("%d",&a[i]);
 }
 ptr=a;
 printf("enter element to be searched:");
 scanf("%d",&key);
  for(i=0;i<n;i++)
  {
   if(*(ptr+i)==key)
   {
    printf("element %d found at posn %d",key,i+1);
   f=1;
   break;
   }
  }
   if(f!=1)
   {
    printf("element %d not found",key);
   }
 }
  
   
