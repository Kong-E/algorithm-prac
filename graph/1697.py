import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

visited = [False] * 100001

queue = deque([(n,0)])
visited[n] = True

while queue:
  node, time = queue.popleft()
      
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