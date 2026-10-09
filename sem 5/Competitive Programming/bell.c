#include <stdio.h>
 #define MAX 10
 #define INF 999
int main() {
 int graph[MAX][MAX];
 int distance[MAX];
 int n, source;
int i, j, k;
 printf("Enter number of vertices: ");
scanf("%d", &n);
 printf("Enter adjacency matrix:\n");
for (i = 0; i < n; i++) {
for (j = 0; j < n; j++) {
scanf("%d", &graph[i][j]); } }
printf("Enter source vertex: ");
scanf("%d", &source);
for (i = 0; i < n; i++) {
distance[i] = INF; }
distance[source] = 0;
for (k = 1; k <= n - 1; k++) {
for (i = 0; i < n; i++) {
for (j = 0; j < n; j++) {
if (graph[i][j] != 0 && distance[i] != INF && distance[i] + graph[i][j] < distance[j]) { distance[j] = distance[i] + graph[i][j]; } } } }
for (i = 0; i < n; i++) {
 for (j = 0; j < n; j++) {
 if (graph[i][j] != 0 && distance[i] != INF && distance[i] + graph[i][j] < distance[j]) {
printf("\nNegative weight cycle exists.\n");
return 0; } } }
 printf("\nShortest distances from vertex %d:\n", source);
 for (i = 0; i < n; i++) {
 printf("To vertex %d = %d\n", i, distance[i]); }
 return 0; }
