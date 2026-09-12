#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Node {
    struct Node *child[26];
    int end;
};

struct Node *newNode() {
    struct Node *p = calloc(1, sizeof(struct Node));
    return p;
}

void insert(struct Node *root, char *word) {
    struct Node *p = root;

    for (int i = 0; word[i]; i++) {
        int x = word[i] - 'a';

        if (p->child[x] == NULL)
            p->child[x] = newNode();

        p = p->child[x];
    }
    p->end = 1;
}

int search(struct Node *root, char *word) {
    struct Node *p = root;

    for (int i = 0; word[i]; i++) {
        int x = word[i] - 'a';

        if (p->child[x] == NULL)
            return 0;

        p = p->child[x];
    }
    return p->end;
}

int main() {
    struct Node *root = newNode();

    insert(root, "cat");
    insert(root, "car");
    insert(root, "dog");

    printf("%s\n", search(root, "cat") ? "Found" : "Not Found");
    printf("%s\n", search(root, "cow") ? "Found" : "Not Found");

    return 0;
}
