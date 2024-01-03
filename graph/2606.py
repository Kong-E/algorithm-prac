from collections import deque

n = int(input())  # Assuming n is a single integer
k = int(input())  # Assuming k is a single integer
graph = {i+1: [] for i in range(n)}
visited = [0] * (n+1)

for _ in range(k):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
def bfs(start_node):
    queue = deque([start_node])
    visited[start_node] = 1
    
    while queue:
        node = queue.popleft()
        
        for adj_node in graph[node]:
            if visited[adj_node] == 0:
                queue.append(adj_node)
                visited[adj_node] = 1
    
bfs(1)
print(sum(visited)-1)