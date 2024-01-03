import sys

sys.setrecursionlimit(10000)

n = int(input())  # Assuming n is a single integer
k = int(input())  # Assuming k is a single integer
graph = {i+1: [] for i in range(n)}
visited = [False] * (len(graph)+1)
count = 0

for _ in range(k):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
def dfs(start_node):
    global count
    visited[start_node] = True
    
    for adj_node in graph[start_node]:
        if not visited[adj_node]:
            count += 1
            dfs(adj_node)
            
    return count
    
print(dfs(1))