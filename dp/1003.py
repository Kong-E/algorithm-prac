t = int(input()) # 테스트 케이스 개수
n_list = []
count = [0, 0]

for _ in range(t):
    i = int(input())
    n_list.append(i)
    
def fibonacci(n, d):
    if n == 0:
        count[0] += 1
        return 0
    if n == 1:
        count[1] += 1
        return 1
    if d[n] != 0:
        return d[n]
    d[n] = fibonacci(n-1, d) + fibonacci(n-2, d)
    return d[n]
    
for n in n_list:
    d = [0] * (n+1)
    fibonacci(n, d)
    print(count[0], count[1])
    count = [0, 0]