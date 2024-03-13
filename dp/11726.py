import sys

input = sys.stdin.readline

n = int(input())

memo = [0]*(n+1)

# 탑 다운
def answer(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    if memo[n] != 0:
        return memo[n]
    
    memo[n] = (answer(n-1) + answer(n-2))%10007
    return memo[n]

print(answer(n))