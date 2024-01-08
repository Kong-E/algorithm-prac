from collections import deque

M, N, H = map(int, input().split())

dx = [0, 0, -1, 1, 0, 0]
dy = [1, -1, 0, 0, N, -N]

graph = [[] for _ in range(N * H)]

for i in range(H):
  for j in range(N):
      a = list(map(int, input().split()))
      graph[j + (i * N)] = a

def bfs():
  queue = deque()
  max_day = 0

  # 초기 익은 토마토 위치 찾기
  for i in range(N * H):
    for j in range(M):
      if graph[i][j] == 1:
        queue.append((j, i, 0))

  while queue:
    x, y, day = queue.popleft()
    max_day = max(max_day, day)

    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= M or ny < 0 or ny >= N * H:
        continue
      if (ny == y + 1 or ny == y - 1) and ny // N != y // N:
        continue
      if graph[ny][nx] != 0:
        continue

      queue.append((nx, ny, day + 1))
      graph[ny][nx] = 1  # 익은 상태로 변경

  return max_day

max_value = bfs()

# 모든 칸을 확인하여 익지 않은 토마토가 있는지 확인
unripe_exist = any(0 in row for row in graph)

if unripe_exist:
    print(-1)
elif max_value == 0:
    print(0)
else:
    print(max_value)
