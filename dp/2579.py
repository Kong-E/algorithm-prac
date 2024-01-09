import sys

# input 함수를 재정의하지 않고, 사용할 때마다 rstrip()을 적용합니다.
def input():
    return sys.stdin.readline().rstrip()

n = int(input())  # 계단의 개수
stairs = [0] * (n + 1)

for i in range(1, n + 1):
    stairs[i] = int(input())
    
# dp 배열을 초기화합니다.
dp = [0] * 301
dp[1] = stairs[1]
if n >= 2:
    dp[2] = stairs[1] + stairs[2]
if n >= 3:
    dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

# 점화식을 계산합니다.
for i in range(4, n + 1):
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

print(dp[n])