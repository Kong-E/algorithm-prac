import sys

input = sys.stdin.readline

x = int(input())
arr = [64]

while sum(arr) > x:
    arr.sort()  # 리스트를 정렬하여 가장 작은 요소를 찾습니다.
    m = arr[0]
    arr.pop(0)  # 가장 작은 요소를 제거합니다.
    half = m / 2
    if sum(arr) + half >= x:
        arr.append(half)
    else:
        arr.append(half)
        arr.append(half)

print(len(arr)) 