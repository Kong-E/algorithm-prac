import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
count = 0
max_count = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start_node, board, visited):
    global dx, dy
    queue = deque([start_node])
    visited[start_node[1]][start_node[0]] = True
    count = 0

    while queue:
        x, y = queue.popleft()
        count += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
            if board[ny][nx] == 1 and not visited[ny][nx]:
                queue.append((nx, ny))
                visited[ny][nx] = True

    return count

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            max_count = max(max_count, bfs((j, i), board, visited))
            count += 1

print(count)
print(max_count)