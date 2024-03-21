import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
answer = 1e9

arr.sort(reverse=True)

for i in range(n):
    for j in range(i, n):
        sub = abs(arr[i]-arr[j])
        if sub >= m:
            answer = min(answer, sub)

print(answer)