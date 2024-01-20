import sys
from collections import Counter

N = int(input())
N_list = list(map(int, sys.stdin.readline().split()))

M = int(input())
M_list = list(map(int, sys.stdin.readline().split()))

count_N_list = Counter(N_list)

for i in M_list:
    print(count_N_list[i], end=' ')