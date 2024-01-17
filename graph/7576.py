import sys
from collections import deque

input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

m, n = map(int, input().split())
graph = []

for I in range(n):
  graph.append(list(map(int,input().split())))
  
queue = deque()
max_value = 0

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      queue.append((i,j,0))
      
while queue:
  x, y, day = queue.popleft()
  max_value = max(max_value, day)
    
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
      continue
    if graph[nx][ny] != 0:
      continue
    
    queue.append((nx,ny,day+1))
    graph[nx][ny] = 1
    
unripen_exist = any(0 in row for row in graph)

if unripen_exist:
    print(-1)
elif max_value == 0:
    print(0)
else:
    print(max_value)
