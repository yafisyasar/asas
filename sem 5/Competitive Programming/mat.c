#include <stdio.h>

int main()
{
    int a[10][10], b[10][10], c[10][10];
    int i, j, k;
    int r1, c1, r2, c2;

    printf("Enter rows and columns of first matrix: ");
    scanf("%d %d", &r1, &c1);

    printf("Enter rows and columns of second matrix: ");
    scanf("%d %d", &r2, &c2);

    if (r1 < 1 || r1 > 10 || c1 < 1 || c1 > 10 ||
        r2 < 1 || r2 > 10 || c2 < 1 || c2 > 10)
    {
        printf("Invalid matrix size!\n");
        return 0;
    }

    printf("Enter elements of first matrix:\n");
    for (i = 0; i < r1; i++)
    {
        for (j = 0; j < c1; j++)
        {
            scanf("%d", &a[i][j]);
        }
    }

    printf("Enter elements of second matrix:\n");
    for (i = 0; i < r2; i++)
    {
        for (j = 0; j < c2; j++)
        {
            scanf("%d", &b[i][j]);
        }
    }

    /* Matrix Addition */
    if (r1 == r2 && c1 == c2)
    {
        printf("\nMatrix Addition:\n");

        for (i = 0; i < r1; i++)
        {
            for (j = 0; j < c1; j++)
            {
                c[i][j] = a[i][j] + b[i][j];
                printf("%d ", c[i][j]);
            }
            printf("\n");
        }
    }
    else
    {
        printf("\nMatrix addition is not possible.\n");
    }

    /* Matrix Multiplication */
    if (c1 == r2)
    {
        printf("\nMatrix Multiplication:\n");

        for (i = 0; i < r1; i++)
        {
            for (j = 0; j < c2; j++)
            {
                c[i][j] = 0;

                for (k = 0; k < c1; k++)
                {
                    c[i][j] += a[i][k] * b[k][j];
                }
            }
        }

        for (i = 0; i < r1; i++)
        {
            for (j = 0; j < c2; j++)
            {
                printf("%d ", c[i][j]);
            }
            printf("\n");
        }
    }
    else
    {
        printf("\nMatrix multiplication is not possible.\n");
    }

    /* Transpose of First Matrix */
    printf("\nTranspose of First Matrix:\n");

    for (i = 0; i < c1; i++)
    {
        for (j = 0; j < r1; j++)
        {
            printf("%d ", a[j][i]);
        }
        printf("\n");
    }

    return 0;
}