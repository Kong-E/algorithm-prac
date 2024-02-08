n = int(input())

print((1<<n)-1)

def hanoi(n, start, end):
	if n == 0:
		return
	
	mid = 6 - start - end
	
	hanoi(n-1, start, mid)
	print(start, end)
	hanoi(n-1, mid, end)
	
hanoi(n,1,3)