#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, *p;
    scanf("%d", &n);
    p = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++)
        p[i] = i + 1;
    n = 10;
    p = realloc(p, n * sizeof(int));
    if (p == NULL)
        return 1;
    for (int i = 5; i < n; i++)
        p[i] = i + 1;
    for (int i = 0; i < n; i++)
        printf("%d ", p[i]);
    free(p);
    return 0;
}