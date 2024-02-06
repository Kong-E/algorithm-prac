import sys
from collections import deque

input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

t = int(input())

def bfs(queue, board, w, h, dist):
	while queue:
		x, y, d = queue.popleft()
		d_ = d+1 if d > 0 else d-1
		
		if d < 0 and (x == 0 or x == w-1 or y == 0 or y == h-1):
			return -d
		
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if nx < 0 or nx >= w or ny < 0 or ny >= h:
				continue
			if board[ny][nx] == '.' and dist[ny][nx] == 0:
				queue.append((nx,ny,d_))
				dist[ny][nx] = d
				
	return "IMPOSSIBLE"

for _ in range(t):
	queue = deque()
	w, h = map(int, list(input().split()))
	board = []
	dist = [[0]*w for _ in range(h)]
	
	for _ in range(h):
		board.append(list(input().rstrip()))
		
	for i in range(h):
		for j in range(w):
			if board[i][j] == '@':
				board[i][j] = '.'
				temp_i = i
				temp_j = j
			if board[i][j] == '*':
				queue.append((j,i,1))
				dist[i][j] = 1
	
	queue.append((temp_j,temp_i,-1))
				
	print(bfs(queue, board, w, h, dist))
		
	