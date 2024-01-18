import sys

input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

m, n, k = map(int, input().split())

graph = [[0] * n for _ in range(m)]

for _ in range(k):
  x1, y1, x2, y2 = map(int, input().split())
  
  for i in range(y1, y2):
    for j in range(x1, x2):
      graph[i][j] = 1
      
queue = []
answer = []

for i in range(m):
  for j in range(n):
    if graph[i][j] == 0:
      queue.append((i,j))
      graph[i][j] = 1
      count = 1
      
      while queue:
        x, y = queue.pop(0)
        
        for k in range(4):
          nx = x + dx[k]
          ny = y + dy[k]
          
          if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
          if graph[nx][ny] != 0:
            continue
          
          queue.append((nx,ny))
          graph[nx][ny] = 1
          count += 1
          
      answer.append(count)
      
answer.sort()

print(len(answer))
for i in range(len(answer)):
  print(answer[i], end = ' ')