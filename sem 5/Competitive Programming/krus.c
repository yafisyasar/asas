#include <stdio.h>
#define MAX 10
int graph[MAX][MAX];
 int mst[MAX][MAX];
int n;
 int findPath(int u, int v, int visited[]) {
int i;
 if (u == v)
return 1;
visited[u] = 1;
for (i = 0; i < n; i++) {
if (mst[u][i] != 0 && visited[i] == 0) {
 if (findPath(i, v, visited))
 return 1; } }
 return 0;
}
int main() {
int i, j;
int u, v, min;
 int edges = 0;
int cost = 0;
 int visited[MAX];
printf("Enter number of vertices: ");
scanf("%d", &n);
printf("Enter adjacency matrix:\n");
for (i = 0; i < n; i++) {
for (j = 0; j < n; j++) {
scanf("%d", &graph[i][j]);
mst[i][j] = 0; } }
printf("\nEdges selected for MST:\n");
while (edges < n - 1) {
min = 999; for (i = 0; i < n; i++) {
for (j = i + 1; j < n; j++) {
 if (graph[i][j] != 0 && graph[i][j] < min) {
 min = graph[i][j];
 u = i;
v = j; } } }
graph[u][v] = 0;
graph[v][u] = 0;
for (i = 0; i < n; i++)
 visited[i] = 0;
if (!findPath(u, v, visited)) {
mst[u][v] = min;
mst[v][u] = min;
 printf("%d -- %d = %d\n", u, v, min);
cost += min; edges++; } }
 printf("\nMinimum Cost = %d\n", cost);
return 0; }
