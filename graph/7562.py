import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

dx = [1,1,2,2,-1,-1,-2,-2]
dy = [2,-2,1,-1,2,-2,1,-1]

graph = []

def bfs(start_x, start_y, target_x, target_y):
  counts = []
  queue = deque([(start_x, start_y, 0)])
  graph[start_x][start_y] = 1
  
  while queue:
    x, y, count = queue.popleft()

    if (x, y) == (target_x, target_y):
      counts.append(count)
    
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if nx < 0 or nx >= m or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] == 0:
        queue.append((nx, ny, count + 1))
        graph[nx][ny] = 1  
        
  print(counts)
  return min(counts)

for _ in range(n):
  m = int(input())
  graph = [[0]*m for _ in range(m)]
  
  current = tuple(map(int, input().split()))
  target = tuple(map(int, input().split()))
  
  print(bfs(current[0], current[1], target[0], target[1]))