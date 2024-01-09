import sys
import math

input = sys.stdin.readline

n = int(input())

dp = [0] * 1001

def number_of_combinations(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

dp[1] = 10

for i in range(2, n+1):
    dp[i] = dp[i-1] + number_of_combinations(9+i-1, i)
    
print(dp[n]%10007)