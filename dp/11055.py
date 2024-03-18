import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))

dp = [0]*n
for i in range(n):
    dp[i] = a[i]
    for j in range(i): # i 이전까지만 탐색
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j]+a[i])

print(max(dp))
# print(dp)