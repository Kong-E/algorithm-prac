import sys

input = sys.stdin.readline

n, m = map(int, input().split())
tall_graph = {i+1: [] for i in range(n)}
small_graph = {i+1: [] for i in range(n)}
cnt = 0

for _ in range(m):
	a, b = map(int, input().split())
	tall_graph[a].append(b)
	small_graph[b].append(a)
	
def dfs(graph, start_node, visited):
	if visited[start_node]:
		return 0
	visited[start_node] = True
	
	cnt = 1
	for node in graph[start_node]:
		cnt += dfs(graph, node, visited)
		
	return cnt

for i in range(1, n+1):
	tall_visited = {j+1: False for j in range(n)}
	tall_cnt = dfs(tall_graph, i, tall_visited) - 1
	
	small_visited = {j+1: False for j in range(n)}
	small_cnt = dfs(small_graph, i, small_visited) - 1
	# print(tall_cnt, small_cnt)
	
	if tall_cnt+small_cnt == n-1:
		cnt += 1
	
print(cnt)
print(tall_graph)
print(small_graph)