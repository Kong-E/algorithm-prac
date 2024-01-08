from collections import deque

M,N,H = map(int,input().split())

dx = [0,0,-1,1,0,0]
dy = [1, -1, 0, 0, N, -N]

graph = [[] for _ in range(N*H)]

for i in range(H):
  for j in range(N):
      a = list(map(int, input().split()))
      graph[j+(i*N)] = a

def bfs(start_x,start_y): # x = m (열), y = n (행)
  queue = deque([(start_x, start_y, 0)])  # 좌표와 날짜를 함께 큐에 저장

  while queue:
    x, y, day = queue.popleft()

    for i in range(6): # 얘네는 하루 걸림 -> 다 돌고 난 후에 count += 1
      nx = x + dx[i]
      ny = y + dy[i] # dy가 1이거나 -1일 때 같은 층이어야 함을 고려해야함 !!!!

      # 범위를 벗어나면 건너뜀
      if nx < 0 or nx >= M or ny < 0 or ny >= N*H:
        continue
      # 같은 층이 아니면 건너뜀
      if (ny == y + 1 or ny == y - 1) and ny // N != y // N:
        continue
      # 토마토가 들어있지 않은 칸이면 건너 뜀
      if graph[ny][nx] == -1: 
        continue
      queue.append((nx, ny, day + 1))
      graph[ny][nx] = day + 1  # 날짜로 갱신

for i in range(N*H):
   for j in range(M):
      if graph[i][j] == 1:
        bfs(j,i)
         
max_value = 0 
unripe_exist = False

for row in graph:
    for element in row:
        if element == 0:
          unripe_exist = True
        if element > max_value:
            max_value = element

# # 그래프 출력
# for node in graph:
#     print(node)

if unripe_exist:
  print(-1)
elif max_value == 1:
  print(0)
else:
  print(max_value)