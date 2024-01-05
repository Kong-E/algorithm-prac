from collections import deque

M,N,H = map(int,input().split())

dx = [0,0,-1,1,0,0]
dy = [1, -1, 0, 0, H, -H]

graph = [[] for _ in range(N*H)]
visited = [[False for _ in range(M)] for _ in range(N*H)]

for i in range(H):
  for j in range(N):
      a = list(map(int, input().split()))
      graph[j+(i*N)] = a

def bfs(start_x,start_y): # x = m (열), y = n (행)
  queue = deque([(start_x,start_y)])
  visited[start_y][start_x] = True

  while queue:
    (x, y) = queue.popleft()

    for i in range(6): # 얘네는 하루 걸림 -> 다 돌고 난 후에 count += 1
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= M or ny < 0 or ny >= N*H:
          continue
      if graph[ny][nx] == -1 or visited[ny][nx]:
          continue
      if graph[ny][nx] == 0:
        queue.append((nx,ny))
        graph[ny][nx] = graph[y][x] + 1
        visited[ny][nx] = True

for i in range(N*H):
   for j in range(M):
      if graph[i][j] == 1 and not visited[i][j]:
        bfs(j,i)
         
max_value = 0 
unripe_exist = False

for row in graph:
    for element in row:
        if element == 0:
          unripe_exist = True
        if element > max_value:
            max_value = element

if unripe_exist:
  print(-1)
else:
  print(max_value-1)