import sys

input = sys.stdin.readline

n = int(input())

channels = [input().rstrip() for _ in range(n)]

idx1, idx2 = channels.index('KBS1'), channels.index('KBS2')

if idx1 > idx2:
    idx2 += 1 # KBS1이 올라가는 과정에서 KBS2가 내려가므로
    
print('1'*idx1 + '4'*idx1 + '1'*idx2 + '4'*(idx2-1))
# print(channels)