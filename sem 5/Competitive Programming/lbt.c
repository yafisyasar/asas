#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

struct Node* createNode(int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

struct Node* buildTree(int arr[], int n, int i) {
    struct Node* root = NULL;

    if (i < n) {
        root = createNode(arr[i]);
        root->left = buildTree(arr, n, 2 * i + 1);
        root->right = buildTree(arr, n, 2 * i + 2);
    }
    return root;
}

void printTree(struct Node* root) {
    if (root == NULL) return;
    printf("\nNode = %d", root->data);
    if (root->left != NULL)
        printf("\nLeft Child = %d", root->left->data);
    else
        printf("\nLeft Child = NULL");
    if (root->right != NULL)
        printf("\nRight Child = %d", root->right->data);
    else
        printf("\nRight Child = NULL");
    printf("\n");
    printTree(root->left);
    printTree(root->right);
}

int main() {
    int n;
    printf("Enter number of nodes: ");
    if (scanf("%d", &n) != 1 || n <= 0) return 1;
    int temp_arr[n];
    printf("Enter values: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &temp_arr[i]);
    }
    struct Node* root = buildTree(temp_arr, n, 0);
    printf("\ntree rep");
    printTree(root);

    return 0;
}
