import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
answer = 2e9

arr.sort()

left, right = 0, 0

while left <= right and right < n:
    subt = arr[right]-arr[left]
    if subt < m:
        right += 1
    else:
        answer = min(answer, subt)
        left += 1

print(answer)