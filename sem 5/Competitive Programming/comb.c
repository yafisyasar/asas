#include <stdio.h>

int main()
{
    int n, r, i;
    int nf = 1, rf = 1, nrf = 1;
    int result;

    printf("Enter n and r: ");
    scanf("%d %d", &n, &r);

    for (i = 1; i <= n; i++)
        nf = nf * i;

    for (i = 1; i <= r; i++)
        rf = rf * i;

    for (i = 1; i <= n - r; i++)
        nrf = nrf * i;

    result = nf / (rf * nrf);

    printf("Number of ways = %d", result);

    return 0;
}