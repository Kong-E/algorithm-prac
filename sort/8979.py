import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
count = 1
q = []

for _ in range(n):
  a, b, c, d = map(int, input().split())
  if a == k:
    target = (-b,-c,-d)
  heapq.heappush(q, (-b,-c,-d))
  
while q:
  tup = heapq.heappop(q)
  if tup == target:
    print(count)
    break
  else:
    count += 1