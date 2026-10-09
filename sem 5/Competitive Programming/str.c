#include <stdio.h>
#include <string.h>

int main()
{
    char text[200], pattern[100];
    int i, j, found = 0;
    int textLen, patternLen;

    printf("Enter the text string: ");
    fgets(text, sizeof(text), stdin);

    printf("Enter the pattern string: ");
    fgets(pattern, sizeof(pattern), stdin);

    /* Remove newline characters */
    text[strcspn(text, "\n")] = '\0';
    pattern[strcspn(pattern, "\n")] = '\0';

    textLen = strlen(text);
    patternLen = strlen(pattern);

    if (patternLen == 0)
    {
        printf("Pattern cannot be empty.\n");
        return 0;
    }

    for (i = 0; i <= textLen - patternLen; i++)
    {
        for (j = 0; j < patternLen; j++)
        {
            if (text[i + j] != pattern[j])
            {
                break;
            }
        }

        if (j == patternLen)
        {
            printf("Pattern found at position %d\n", i + 1);
            found = 1;
        }
    }

    if (!found)
    {
        printf("Pattern not found.\n");
    }

    return 0;
}