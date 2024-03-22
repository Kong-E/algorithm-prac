import sys

input = sys.stdin.readline

n = int(input())
result = []
count = 0

def move(start, end):
    global count
    result.append((start, end))
    count += 1

def hanoi(n, start, end, sub):
    if n == 1:
        move(start, end)
    else:
        hanoi(n-1, start, sub, end)
        move(start, end)
        hanoi(n-1, sub, end, start)

hanoi(n, 1, 3, 2)

print(count)
for a, b in result:
    print(a, b)