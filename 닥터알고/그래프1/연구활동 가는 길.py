import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int,input().split()) 
minDistance = [INF]*(n+1)
graph = {i+1: [] for i in range(n)}

for _ in range(m): 
	a, b, c = map(int, input().split())
	graph[a].append((b,c))
	graph[b].append((a,c))

def dfs(v, d):
	if minDistance[v] !=  0 and minDistance[v] < d:
		return
	minDistance[v] = d
	for i in graph[v]:
		dfs(i[0], d+i[1])
		
dfs(1,1)

print(minDistance[n]-1)