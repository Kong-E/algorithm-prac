import sys
import itertools

input = sys.stdin.readline

n, m = map(int, input().split())

items = list(range(1,n+1))

all_permutations = list(itertools.permutations(items, m))

for perm in all_permutations:
  for p in perm:
    print(p, end=' ')
  print()