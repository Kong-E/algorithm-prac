import sys
from collections import deque

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
answer = 0

def bfs(start_node, board):
    visited = [[False]*m for _ in range(n)]

    sx, sy, scnt = start_node
    queue = deque([(sx, sy, scnt)])
    visited[sy][sx] = True
    max_cnt = 0

    while queue:
        x, y, cnt = queue.popleft()

        max_cnt = max(max_cnt, cnt)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
            if board[ny][nx] == 'L' and not visited[ny][nx]:
                queue.append((nx, ny, cnt+1))
                visited[ny][nx] = True

    return max_cnt
    
for i in range(n):
    for j in range(m):
        if board[i][j] == 'L':
            answer = max(answer, bfs((j, i, 0), board))

print(answer)
