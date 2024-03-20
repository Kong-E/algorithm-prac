import sys

input = sys.stdin.readline
t = int(input())
arr = [int(input()) for _ in range(t)]
dp = [0]*(11)

# 1, 2, 3의 합으로 나타내는 방법의 수
dp[1] = 1 # 1
dp[2] = 2 # 2 // 1+1
dp[3] = 4 # 3 // 1+2 // 1+1+1, 2+1
# dp[4] = 7 # 1+3 // 1+1+2, 2+2 // 3+1, 1+2+1, 1+1+1+1, 2+1+1 
# dp[5] = 13 # 2+3, 1+1+3 // 3+2, 1+2+2, 1+1+1+2, 2+1+2 // 1+3+1, 1+1+2+1, 2+2+1, 3+1+1, 1+2+1+1, 1+1+1+1+1, 2+1+1+1

def top_down(number):
    if number <= 0:
        return 0
    if dp[number] == 0:
        dp[number] = top_down(number-3)+top_down(number-2)+top_down(number-1)
    return dp[number]

for number in arr:
    print(top_down(number))