import sys
import heapq

input = sys.stdin.readline

n = int(input())
q = []
seen = set()

for _ in range(n):
    my_str = input().rstrip()
    if my_str not in seen:
        seen.add(my_str)
        heapq.heappush(q, (len(my_str), my_str))
    
while q:
    _, str_val = heapq.heappop(q)
    print(str_val)