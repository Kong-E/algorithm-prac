import sys

input = sys.stdin.readline
n = int(input())
water = list(map(int, input().split()))
count = 0
check = [False]*(sum(water)+1)

def dfs(index, sum, n):
    if index == n:
        if sum > 0:
            check[sum] = True
        return
    dfs(index+1, sum+water[index], n)
    dfs(index+1, sum-water[index], n)
    dfs(index+1, sum, n)

dfs(0, 0, n)

for i in range(1, sum(water)+1):
    if not check[i]:
        count += 1

print(count)