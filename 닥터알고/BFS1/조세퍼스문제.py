import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
people = deque(list(range(1, n+1)))

while len(people) != 0:
	for i in range(1,m):
		person = people.popleft()
		people.append(person)
		
	person = people.popleft()
	print(person, end=' ')
