import sys
from collections import deque

input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
result = 0

def bfs(start, end, visited):
    global result
    queue = deque([start])
    visited[start] = True

    while queue:
        result += 1
        for _ in range(len(queue)):
            v = queue.popleft()
            if v == end:
                return
            if v + U <= F and not visited[v + U]:
                queue.append(v + U)
                visited[v + U] = True
            if v - D > 0 and not visited[v - D]:
                queue.append(v - D)
                visited[v - D] = True

    result = 'use the stairs'
    
visited = [False] * (F + 1)
bfs(S, G, visited)
if result == 'use the stairs':
    print(result)
else:
    print(result - 1)