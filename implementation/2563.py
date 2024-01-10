import sys

input = sys.stdin.readline

n = int(input())
papers = []
cross = 0

for _ in range(n):
    a, b = map(int, input().split())
    papers.append([a, b])
    
for i in range(n):
    for j in range(i+1, n):
        v = sorted([papers[j][0],papers[i][0]])
        h = sorted([papers[j][1],papers[i][1]])
        if v[1]-v[0] < 10 and h[1]-h[0] < 10:
            cross += (v[0]+10-v[1])*(h[0]+10-h[1])
            
print(n*100-cross)