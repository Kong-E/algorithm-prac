import sys

input = sys.stdin.readline

n, k = map(int, input().split())

queue = [(n, 0)]
visited = [False] * 100001

while queue:
  node, time = queue.pop(0)
      
  if node - 1 >= 0 and not visited[node-1]:
    queue.append((node-1, time+1))
    visited[node-1] = True
  if node + 1 <= 100000 and not visited[node+1]:
    queue.append((node+1, time+1))
    visited[node+1] = True
  if node * 2 <= 100000 and not visited[node*2]:
    queue.append((node*2, time+1))
    visited[node*2] = True
    
  if node == k:
    print(time)
    break