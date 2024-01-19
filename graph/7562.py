import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

dx = [1,1,2,2,-1,-1,-2,-2]
dy = [2,-2,1,-1,2,-2,1,-1]

graph = []

def bfs(start_node, target_node):
  queue = deque([start_node])
  graph[start_node[0]][start_node[1]] = 1
  
  while queue:
    x, y = queue.popleft()

    if (x, y) == target_node:
      return graph[x][y] - 1
    
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if nx < 0 or nx >= m or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] == 0:
        queue.append((nx, ny))
        graph[nx][ny] = graph[x][y] + 1

for _ in range(n):
  m = int(input())
  graph = [[0]*m for _ in range(m)]
  
  current = tuple(map(int, input().split()))
  target = tuple(map(int, input().split()))
  
  print(bfs(current, target))