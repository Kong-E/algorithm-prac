from bisect import bisect_left, bisect_right
from sys import stdin

n = stdin.readline().rstrip()
card = list(map(int,stdin.readline().split()))
m = stdin.readline().rstrip()
test = list(map(int,stdin.readline().split()))

card.sort()

for i in range(len(test)):
    print(bisect_right(card, test[i]) - bisect_left(card, test[i]), end=' ')