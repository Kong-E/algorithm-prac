x_arr = [0, 0, -1, 1]
y_arr = [1, -1, 0, 0]

def dfs_iterative(graph, x, y, visited):
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        if not visited[x][y]:
            visited[x][y] = True
            for idx in range(4):
                nx = x + x_arr[idx]
                ny = y + y_arr[idx]
                if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and graph[nx][ny] == 1 and not visited[nx][ny]:
                    stack.append((nx, ny))

T = int(input())
result = []

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(N)] for _ in range(M)]
    visited = [[False for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    count = 0
    for x in range(M):
        for y in range(N):
            if graph[x][y] == 1 and not visited[x][y]:
                dfs_iterative(graph, x, y, visited)
                count += 1

    result.append(count)

for count in result:
    print(count)