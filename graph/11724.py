import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = { i: [] for i in range(1, n+1)}
visited = { i: False for i in range(1, n+1)}

count = 0

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  
def bfs(start_node):
  queue = deque([start_node])
  visited[start_node] = True
  
  while queue:
    node = queue.popleft()
    
    for adj_node in graph[node]:
      if not visited[adj_node]:
        queue.append(adj_node)
        visited[adj_node] = True
  
for i in range(1, n+1):
  if not visited[i]:
    bfs(i)
    count += 1

print(count)