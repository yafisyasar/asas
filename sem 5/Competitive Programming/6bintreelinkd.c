#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *left, *right;
};
struct Node* create(int x) {
    struct Node *p = malloc(sizeof(struct Node));
    p->data = x;
    p->left = p->right = NULL;
    return p;
}
int main() {
    struct Node *root;
    root = create(10);
    root->left = create(20);
    root->right = create(30);
    printf("Root = %d\n", root->data);
    printf("Left = %d\n", root->left->data);
    printf("Right = %d\n", root->right->data);
    return 0;
}