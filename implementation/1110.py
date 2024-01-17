import sys

input = sys.stdin.readline

n = input().rstrip()

arr = [n]

for i, a in enumerate(arr):
  if int(a) == int(n) and i != 0:
    continue
  if len(a) == 1:
    a = '0' + a
  arr.append(a[1]+str(int(a[0])+int(a[1]))[-1])
  
print(len(arr)-1)