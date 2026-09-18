#include <stdio.h>

int main() {
    int a[10], n, key, low, high, mid;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        scanf("%d", &a[i]);
    scanf("%d", &key);
    low = 0;
    high = n - 1;
    while (low <= high) {
        mid = (low + high) / 2;
        if (a[mid] == key) {
            printf("Found");
            return 0;
        }
        else if (key < a[mid])
            high = mid - 1;
        else
            low = mid + 1;
    }
    printf("Not Found");
    return 0;
}