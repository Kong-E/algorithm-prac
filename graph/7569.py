from collections import deque

M,N,H = map(int,input().split())

dx = [0,0,-1,1,-H,H]
dy = [1,-1,0,0,0,0]

graph = [[] for _ in range(N*H)]
# visited = [[False for _ in range(M)] for _ in range(N*H)]
count = 0
day = []

for i in range(H):
  for j in range(N):
      a = list(map(int, input().split()))
      graph[j+(i*N)] = a

def bfs(start_x,start_y): # x = m (열), y = n (행)
  global count
  queue = deque([(start_x,start_y)])
  # visited[start_y][start_x] = True

  while queue:
    (x, y) = queue.popleft()

    for i in range(6): # 얘네는 하루 걸림 -> 다 돌고 난 후에 count += 1
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= M or ny < 0 or ny >= N:
          continue
      if graph[ny][nx] == -1:
          continue
      if graph[ny][nx] == 0:
          queue.append((nx,ny))
          graph[ny][nx] = 1
          # visited[ny][nx] = True
    count += 1

for i in range(N):
   for j in range(M):
      if graph[i][j] == 1:
         bfs(j,i)
         day.append(count)
         count = 0

for list in graph:
  if 0 in list:
    print(-1)
    break
  else:
    print(max(day))
    break