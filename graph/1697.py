import sys

input = sys.stdin.readline

n, k = map(int, input().split())

queue = [(n, 0)]
visited = [False] * 100001

while queue:
  node, time = queue.pop(0)
  
  if not visited[node]:
    visited[node] = True
      
    if node - 1 >= 0:
      queue.append((node-1, time+1))
    if node + 1 <= 100000:
      queue.append((node+1, time+1))
    if node * 2 <= 100000:
      queue.append((node*2, time+1))
      
    if node == k:
      print(time)
      break