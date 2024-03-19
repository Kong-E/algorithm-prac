import math

n = int(input())
arr = list(map(int, input().split()))
count = 0

def is_prime(number):
    if number == 1:
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if number%i == 0:
            return False
    return True

for number in arr:
    if is_prime(number): count += 1
    
print(count)