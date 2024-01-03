from collections import deque

dx=[0,0,-1,1]
dy=[1,-1,0,0]

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))
    
def bfs(start_x,start_y):
    queue = deque([(start_x,start_y)])
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
                
bfs(0,0)
print(graph[N-1][M-1])
        
        