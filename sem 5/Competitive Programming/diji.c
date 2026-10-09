#include <stdio.h>
#define MAX 10
 #define INF 999
 int main() {
 int graph[MAX][MAX];
 int distance[MAX];
int visited[MAX];
 int n, source;
int i, j; int min, u;
 printf("Enter number of vertices: ");
scanf("%d", &n);
printf("Enter adjacency matrix:\n");
 for (i = 0; i < n; i++) {
for (j = 0; j < n; j++) {
scanf("%d", &graph[i][j]); } }
 printf("Enter source vertex: ");
 scanf("%d", &source);
for (i = 0; i < n; i++) {
 distance[i] = INF;
 visited[i] = 0; }
distance[source] = 0;
for (i = 0; i < n - 1; i++) {
min = INF;
u = -1;
for (j = 0; j < n; j++) {
 if (visited[j] == 0 && distance[j] < min) {
min = distance[j]; u = j; } }
visited[u] = 1;
for (j = 0; j < n; j++) {
 if (visited[j] == 0 && graph[u][j] != 0 && distance[u] + graph[u][j] < distance[j]) { distance[j] = distance[u] + graph[u][j]; } } }
 printf("\nShortest distances from vertex %d:\n", source);
 for (i = 0; i < n; i++) {
printf("To vertex %d = %d\n", i, distance[i]); }
return 0; }