#include <stdio.h>
#define MAX 20

int graph[MAX][MAX];
int visited[MAX];
int queue[MAX];
int n;
int front = 0;
int rear = -1;
void BFS(int start)
{
int i;
visited[start] = 1;
queue[++rear] = start;
while (front <= rear)
{
int vertex = queue[front++];
printf("%d ", vertex);
for (i = 0; i < n; i++)
{
if (graph[vertex][i] == 1 && visited[i] == 0)
{
visited[i] = 1;
queue[++rear] = i;
}
}
}
}
int main()
{
int i, j, start;
printf("Enter number of vertices: ");
scanf("%d", &n);
printf("Enter adjacency matrix:\n");
for (i = 0; i < n; i++)
{
for (j = 0; j < n; j++)
{
scanf("%d", &graph[i][j]);
}
}
for (i = 0; i < n; i++)
{
visited[i] = 0;
}
printf("Enter starting vertex (0 to %d): ", n - 1);
scanf("%d", &start);
printf("BFS Traversal: ");
BFS(start);
return 0;
} 
