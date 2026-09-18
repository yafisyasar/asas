#include <stdio.h>

int main() {
    int tree[10], n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        scanf("%d", &tree[i]);
    for (int i = 0; i < n; i++) {
        printf("\nNode = %d", tree[i]);
        if (2*i + 1 < n)
            printf("\nLeft = %d", tree[2*i + 1]);
        else
            printf("\nLeft = NULL");
        if (2*i + 2 < n)
            printf("\nRight = %d", tree[2*i + 2]);
        else
            printf("\nRight = NULL");
    }
    return 0;
}