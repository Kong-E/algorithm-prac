import sys
from collections import deque

input = sys.stdin.readline
t = int(input())

def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def answer(n, home, convenience, festival):
    queue = deque([home])
    visited = [False] * (n + 1)
    # visited[0] = True

    while queue:
        x, y = queue.popleft()
        if distance(x, y, festival[0], festival[1]) <= 1000:
            return 'happy'
        for i in range(n):
            if not visited[i] and distance(x, y, convenience[i][0], convenience[i][1]) <= 1000:
                queue.append(convenience[i])
                visited[i] = True
    return 'sad'

for _ in range(t):
    n = int(input())
    home = tuple(map(int, input().split()))
    convenience = [tuple(map(int, input().split())) for _ in range(n)]
    festival = tuple(map(int, input().split()))
    print(answer(n, home, convenience, festival))

