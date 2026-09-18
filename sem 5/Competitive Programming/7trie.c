#include <stdio.h>
#include <stdlib.h>

struct Node {
    struct Node *child[26];
    int end;
};
struct Node* create() {
    return calloc(1, sizeof(struct Node));
}
void insert(struct Node *root, char *s) {
    for (int i = 0; s[i]; i++) {
        int x = s[i] - 'a';
        if (root->child[x] == NULL)
            root->child[x] = create();
        root = root->child[x];
    }
    root->end = 1;
}
int search(struct Node *root, char *s) {
    for (int i = 0; s[i]; i++) {
        int x = s[i] - 'a';
        if (root->child[x] == NULL)
            return 0;
        root = root->child[x];
    }
    return root->end;
}
int main() {
    struct Node *root = create();
    insert(root, "cat");
    insert(root, "dog");
    printf("%s", search(root, "cat") ? "Found" : "Not Found");
    return 0;
}