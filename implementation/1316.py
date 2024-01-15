import sys

input = sys.stdin.readline

n = int(input())
words = []
check = []
count = 0

for _ in range(n):
    words.append(input().rstrip())
    
for word in words:
    continue_outer_loop = False
    for i in range(len(word)):
        if word[i] not in check:
            check.append(word[i])
        else:
            if i-1 >= 0 and word[i-1] != word[i]:
                continue_outer_loop = True
                check = []
                break
        if i == len(word)-1:
            count += 1
            check = []
    if continue_outer_loop:
        continue
    
print(count)