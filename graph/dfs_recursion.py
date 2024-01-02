def dfs(graph, start_node,visited):
    visited[start_node] = True
    print(start_node)
    
    for adj_node in graph[start_node]: # 인접한 노드 방문
       if not visited[adj_node]:
          dfs(graph,adj_node,visited)
              

# 그래프를 인접 리스트로 표현
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

visited = [False] * (len(graph) + 1)
# DFS 알고리즘 실행
dfs(graph, 1,visited) # 1 2 4 5 3