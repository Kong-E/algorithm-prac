import sys
import copy
from collections import deque

input = sys.stdin.readline

n = int(input())  
graph = [list(input().rstrip()) for _ in range(n)] # 적록색약
graph2 = copy.deepcopy(graph) # 적록색약이 아닌 사람

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
            
visited = [[0] * n for _ in range(n)]
visited2 = [[0] * n for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(start_node, visited, graph):
    queue = deque([start_node])
    visited[start_node[0]][start_node[1]] = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] != graph[x][y]:
                continue
            if visited[nx][ny] == 1:
                continue
            
            queue.append((nx, ny))
            visited[nx][ny] = 1
            
def count(visited, graph):
    count = 0
    
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                bfs((i, j), visited, graph)
                count += 1
                
    return count
  
print(count(visited2, graph2), count(visited, graph))