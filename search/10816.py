import sys

input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))
nlist.sort()

m = int(input())
mlist = list(map(int, input().split()))

ncount = { i : 0 for i in nlist }

for i in nlist:
  ncount[i] += 1
  
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None

for target in mlist:
  result = binary_search(nlist, target, 0, n-1)
  if result == None:
    print(0, end=' ')
  else:
    print(ncount[target], end=' ')