#include <stdio.h>

int isPrime(int n)
{
    int i;
    if (n < 2)
        return 0;
    if (n == 2)
        return 1;
    if (n % 2 == 0)
        return 0;
    for (i = 3; i * i <= n; i += 2)
    {
        if (n % i == 0)
            return 0;
    }
    return 1;
}
int main()
{
    int a, b, i;
    printf("Enter lower and upper limit: ");
    scanf("%d %d", &a, &b);
    printf("Prime numbers between %d and %d are:\n", a, b);
    for (i = a; i <= b; i++)
    {
        if (isPrime(i))
            printf("%d \n", i);
    }
    return 0;
}

