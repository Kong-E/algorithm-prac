import math

def number_of_combinations(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

T = int(input())

nl = []
ml = []

for _ in range(T):
    n, m = map(int, input().split())
    nl.append(n)
    ml.append(m)
    
for i in range(T):
    print(number_of_combinations(ml[i], nl[i]))