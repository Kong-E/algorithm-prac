import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]  # 북, 동, 남, 서 순서
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def clean(x, y, d):
    global total
    if graph[x][y] == 0:
        graph[x][y] = 2  # 청소한 위치는 2로 표시
        total += 1

    for _ in range(4):
        nd = (d + 3) % 4  # 왼쪽 방향으로 회전
        nx, ny = x + dx[nd], y + dy[nd]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            clean(nx, ny, nd)
            return
        d = nd

    # 후진
    nd = (d + 2) % 4
    nx, ny = x + dx[nd], y + dy[nd]
    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 1:
        clean(nx, ny, d)

total = 0
clean(r, c, d)
print(total)