#include <stdio.h>
#define MAX 20
int graph[MAX][MAX];
int visited[MAX];
int n;
void DFS(int vertex){
	int i;
	visited[vertex]=1;
	printf("%d \n",vertex);
	for (i=0;i<n;i++){
		if (graph[vertex][i]==1&&visited[i]==0){
			DFS(i);
		}
	}
}
int main(){
	int i,j,start;
	printf("Enter no. of vertices: ");
	scanf("%d",&n);
	printf("Enter adjacency matrix: ");
	for(i=0;i<n;i++){
		for(j=0;j<n;j++){
			scanf("%d",&graph[i][j]);
		}
	}
	for (i=0;i<n;i++)
		visited[i]=0;
	printf("Enter starting vertex(0 to %d):",n-1);
	scanf("%d",&start);
	printf("DFS Traversal: \n");
	DFS(start);
	return 0;
}
