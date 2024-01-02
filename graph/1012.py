x_arr = [0,0,-1,1]
y_arr = [1,-1,0,0]

T = int(input())
result = [0 for _ in range(T)]

def dfs(graph, x, y, visited):
    # visited[x][y] = True -> dfs 할 것이므로 필요없음
    # 현재 위치에서 상하좌우를 돌아보고 not visited이면 dfs를 한다. 
    # 만약 모두 visited이면 count += 1 한다.
    for idx in range(4):
        nx = x+x_arr[idx]
        ny = y+y_arr[idx]
        if nx >= 0 and ny >= 0 and graph[nx][ny]==1 and not visited[nx][ny]:
            dfs(graph, nx, ny, visited)
    return True
    

for i in range(T):
    count = 0
    
    M, N, K = map(int, input().split())
        
    graph = [[0 for _ in range(N)] for _ in range(M)]
    visited = [[False for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1  # x, y 위치에 1 할당
        
    # 시작점을 뭐로 하지?
    # 카운트는 어떻게 세지?
    if dfs(graph,0,0,visited) == True:
        count += 1
        
    result[i] = count
    
for i in result:
    print(i)

    
        
    
