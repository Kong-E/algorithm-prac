import sys

# Increase the recursion limit if necessary
sys.setrecursionlimit(10000)  # Example, adjust based on your needs

x_arr = [0, 0, -1, 1]
y_arr = [1, -1, 0, 0]

def dfs(graph, x, y, visited):
    if x < 0 or x >= len(graph) or y < 0 or y >= len(graph[0]) or visited[x][y] or graph[x][y] == 0:
        return
    visited[x][y] = True
    for idx in range(4):
        nx = x + x_arr[idx]
        ny = y + y_arr[idx]
        dfs(graph, nx, ny, visited)

T = int(input())
result = []

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(N)] for _ in range(M)]
    visited = [[False for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1  # Marking the cell where there's a '1'

    count = 0
    for x in range(M):
        for y in range(N):
            # Start DFS if the cell is '1' and not visited
            if graph[x][y] == 1 and not visited[x][y]:
                dfs(graph, x, y, visited)
                count += 1  # Increase the count for each connected component found

    result.append(count)

for count in result:
    print(count)