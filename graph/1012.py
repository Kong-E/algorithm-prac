import sys

# Increase the recursion limit if necessary
sys.setrecursionlimit(10000)  # Example, adjust based on your needs

x_arr = [0, 0, -1, 1]
y_arr = [1, -1, 0, 0]

def dfs(graph, x, y, visited):
    visited[x][y] = True  # Mark the current cell as visited
    for idx in range(4):
        nx = x + x_arr[idx]
        ny = y + y_arr[idx]
        # Check for valid adjacent cells and if they are not visited
        if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and graph[nx][ny] == 1 and not visited[nx][ny]:
            dfs(graph, nx, ny, visited)  # Continue DFS for unvisited adjacent cells

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