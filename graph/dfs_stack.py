def dfs(graph, start_node):
    visited = [False] * (len(graph) + 1)
    stack = [start_node]
    
    while stack:
        node = stack.pop()
        
        if not visited[node] :
            visited[node] = True;
            print(node)
            for adj_node in graph[node]: # 인접한 노드 방문
                    if not visited[adj_node]:
                        stack.append(adj_node)
              

# 그래프를 인접 리스트로 표현
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

# DFS 알고리즘 실행
dfs(graph, 1) # 1 3 2 5 4