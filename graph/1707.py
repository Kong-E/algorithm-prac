import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

t = int(input())

def dfs(graph, colors, node, color):
    if colors[node] == color: return True
    if colors[node] == 3 - color: return False
    colors[node] = color

    flag = True
    for adj_node in graph[node]:
        result = dfs(graph, colors, adj_node, 3-color)
        flag &= result

    return flag

for _ in range(t):
    V, E = map(int, input().split())
    colors = { i+1: 0 for i in range(V)}
    graph = { i+1: [] for i in range(V)}

    for _ in range(E):
        u, v = map(int, input().split())
        graph[v].append(u)
        graph[u].append(v)

    for node in range(1, V+1):
        if colors[node] == 0:
            result = dfs(graph, colors, node, 1) # 처음 만나는 노드는 색이 1이라고 전제

            if not result:
                print("NO")
                break

        if node == V:
            print("YES")
        
