import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y, graph, visited):
    global dx, dy
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] > 0 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True

def answer(n, m, graph):
    global dx, dy
    
    year = 0
    while True:
        zero_cnt = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if graph[i][j] > 0:
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            continue
                        if graph[nx][ny] == 0:
                            zero_cnt[i][j] += 1
                    graph[i][j] = max(0, graph[i][j] - zero_cnt[i][j])

        cnt = 0
        visited = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if graph[i][j] > 0 and not visited[i][j]:
                    bfs(i, j, graph, visited)
                    cnt += 1
                    if cnt >= 2:
                        return year + 1           
                
        if cnt == 0:
            return 0
        
        year += 1
    
print(answer(n, m, graph))