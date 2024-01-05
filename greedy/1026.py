import sys

N = int(sys.stdin.readline().rstrip())
A = [int(x) for x in sys.stdin.readline().rstrip().split()]
B = [int(x) for x in sys.stdin.readline().rstrip().split()]
sum = 0

for i in range(N):
    sum += sorted(A)[i] * sorted(B, reverse=True)[i]
    
print(sum)