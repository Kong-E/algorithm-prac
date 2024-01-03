from collections import deque

n = int(input()) # 전체 사람 수
a, b = map(int, input().split()) # 계산해야 하는 두 사람의 번호
m = int(input()) # 부모 자식들 간의 관계의 개수

graph = {i+1:[] for i in range(n)}
visited = [0] * (n+1)
for _ in range(m):
    x, y = map(int, input().split()) # x는 y의 부모
    graph[x].append(y)
    graph[y].append(x)
    
def bfs(start_node, target_node):
    queue = deque([start_node])
    visited[start_node] = 1
    
    while queue:
        node = queue.popleft()
        
        for adj_node in graph[node]:
            if visited[adj_node] == 0:
                queue.append(adj_node)
                visited[adj_node] = 1 
    return -1
                    
# bfs(a,b)

for node in graph:
    print(f"{node} : {graph[node]}")

# 촌수 카운트를 어떻게 하지?
    