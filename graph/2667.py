import sys

sys.setrecursionlimit(10000)

dx=[0,0,-1,1]
dy=[1,-1,0,0]
big_count = 0 # 단지 수 세기
small_count = 1 # 단지 내 아파트 세기
result=[] # 각 단지 아파트 수를 저장하는 리스트

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))
    
def dfs(x,y):
    global small_count
    graph[x][y] = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if graph[nx][ny] == 0:
            continue
        small_count += 1
        dfs(nx,ny)
    return small_count
            
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            result.append(dfs(x,y))
            small_count = 1 # 1로 초기화
            big_count += 1
    
print(big_count)
for i in sorted(result):
    print(i)