import sys

input = sys.stdin.readline
v, e = map(int, input().split())
colors = {i+1: 0 for i in range(v)}
graph = {i+1: [] for i in range(v)}

for _ in range(e):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)
	
def dfs(graph, node, color):
	if colors[node] == color: return True
	if colors[node] == 3-color: return False
	colors[node] = color
	
	flag = True
	for adj_node in graph[node]:
		flag &= dfs(graph, adj_node, 3-color)
		
	return flag

for i in range(1, v+1):
	if colors[i] == 0:
		result = dfs(graph, i, 1)
		
		if not result:
			print("NO")
			break
			
	if i == v:
		print("YES")