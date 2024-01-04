n = int(input()) # 전체 사람 수
a, b = map(int, input().split()) # 계산해야 하는 두 사람의 번호
m = int(input()) # 부모 자식들 간의 관계의 개수

graph = {i+1:[] for i in range(n)}
visited = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split()) # x는 y의 부모
    graph[x].append(y)
    graph[y].append(x)
    
def dfs(start_node, target_node):
    stack = [(start_node, 0)]
    
    while stack:
        (node, count) = stack.pop() 
              
        if visited[node] == 0: 
            visited[node] = 1
                       
            if node == target_node:
                return count  # 타겟 노드에 도달했을 때 촌수 반환

            for adj_node in graph[node]:
                if visited[adj_node] == 0:
                    stack.append((adj_node, count+1))

    return -1  # 타겟 노드에 도달하지 못함
                    
print(dfs(a, b))