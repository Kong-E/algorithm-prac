import sys

sys.setrecursionlimit(10000)

n = int(input())  # Assuming n is a single integer
k = int(input())  # Assuming k is a single integer
graph = {i+1: [] for i in range(n)}
visited = [0] * (n+1)

for _ in range(k):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
def dfs(start_node):
    visited[start_node] = 1
    
    for adj_node in graph[start_node]:
        if visited[adj_node] == 0:
            dfs(adj_node)
    
dfs(1)
print(sum(visited)-1)