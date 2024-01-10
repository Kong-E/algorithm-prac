import sys

input = sys.stdin.readline

n = int(input())
prices = [0] + list(map(int, input().split()))

dp = [0] * (n+1)

dp[1] = prices[1]

for i in range(2, n+1):
    dp[i] = max(dp[i-1]+prices[1], prices[i])
    
print(dp[n])