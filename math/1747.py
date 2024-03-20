import sys
import math

input = sys.stdin.readline
n = int(input())
answer = 0

def is_prime(number):
    if number == 1:
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if number%i == 0:
            return False
    return True

while True:
    if is_prime(n):
        len_n = len(str(n))
        idx = len_n//2
        if len_n % 2 == 0:
            if list(str(n))[:idx][::-1] == list(str(n))[idx:]:
                break
        if len_n % 2 == 1:
            if list(str(n))[:idx][::-1] == list(str(n))[idx+1:]:
                break
    n += 1

print(n)