from collections import deque

def bfs(graph, start_node):
    visited = [False] * (len(graph) + 1)
    queue = deque([start_node])
    visited[start_node] = True # 시작노드 방문 처리
   
    
    while queue:
        node = queue.popleft() # 이어붙인 노드를 꺼냄
        print(node) # 방문 노드 출력
        for adj_node in graph[node]: # 인접한 노드 방문
            if not visited[adj_node]:
                queue.append(adj_node) # 큐에 이어붙임
                visited[adj_node] = True
            
# 그래프를 인접 리스트로 표현
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

# BFS 알고리즘 실행
bfs(graph, 1) # 1, 2, 3, 4, 5