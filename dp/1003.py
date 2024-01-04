import sys

sys.setrecursionlimit(10000)

t = int(input()) # 테스트 케이스 개수
n_list = []
count = [0, 0]

for _ in range(t):
    i = int(input())
    n_list.append(i)
    
def fibonacci(n):
    if n == 0:
        count[0] += 1
        return 0
    if n == 1:
        count[1] += 1
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
    
for n in n_list:
    fibonacci(n)
    print(count[0], count[1])
    count = [0, 0]