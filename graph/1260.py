from collections import deque

N, M, V = map(int, input().split())
graph = {i+1: [] for i in range(N)}

for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(graph, start_node):
    visited = [False] * (len(graph) + 1)
    stack = [start_node]
    result = []

    while stack:
        node = stack.pop()
        
        if not visited[node]:
            visited[node] = True # 현재 노드여야 True 처리를 함
            result.append(str(node))
            for adj_node in sorted(graph[node], reverse=True):
                if not visited[adj_node]:
                    stack.append(adj_node)
    
    return " ".join(result)

def bfs(graph, start_node):
    visited = [False] * (len(graph) + 1)
    queue = deque([start_node]) # 큐에 넣는 순간 존재를 알음
    visited[start_node] = True # 존재를 아는 순간 visited를 True로 설정
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(str(node))
        for adj_node in sorted(graph[node]):
            if not visited[adj_node]:
                queue.append(adj_node)
                visited[adj_node] = True
                
    return " ".join(result)

# DFS 결과를 한 줄로 출력
print(dfs(graph, V))
print(bfs(graph, V))

# # 그래프 출력
# for node in graph:
#     print(f"{node}: {graph[node]}")