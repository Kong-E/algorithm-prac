import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, h, visited):
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        if visited[x][y]:
            continue

        visited[x][y] = True

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] > h:
                stack.append((nx, ny))

result = 0

for h in range(max(map(max, graph))):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > h:
                dfs(i, j, h, visited)
                cnt += 1
    result = max(result, cnt)

print(result)