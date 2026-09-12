#include<stdio.h>
void main()
{
    int n;
    printf("no. of nodes");
    scanf("%d",&n);
    int tree[n];
    printf("enter vals");
    for (int i=0;i<n;i++){
        scanf("%d",&tree[i]);}
        printf("treee rep");
        for (int i=0;i<n;i++){
            printf("\nNode=%d",tree[2*i+1]);
            if(2*i+1<n)
            printf("\nLeft Child=%d",tree[2*i+1]);
            else
            printf("\nLeft Child=NULL");
             if(2*i+2<n)
            printf("\nRight Child=%d",tree[2*i+2]);
            else
            printf("\nRight Child=NULL");
            printf("\n")    ;
        }
return 0;
}