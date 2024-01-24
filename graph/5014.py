import sys
from collections import deque

input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
result = 0

def bfs(start, end):
    visited = [False] * (F + 1)
    queue = deque([(start, 0)])  # (현재 층, 이동 횟수)
    visited[start] = True

    while queue:
        v, count = queue.popleft()
        if v == end:
            return count
        if v + U <= F and not visited[v + U]:
            queue.append((v + U, count + 1))
            visited[v + U] = True
        if v - D > 0 and not visited[v - D]:
            queue.append((v - D, count + 1))
            visited[v - D] = True

    return 'use the stairs'

print(bfs(S, G))