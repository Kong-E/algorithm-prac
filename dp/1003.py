t = int(input()) # 테스트 케이스 개수
n_list = []

for _ in range(t):
    i = int(input())
    n_list.append(i)

for n in n_list:
    s = [0,0] * (n+1) # 0과 1의 개수를 메모이제이션
    
    for i in range(0,n+1):
        if i == 0:
            s[i] = [1, 0]
        elif i == 1:
            s[i] = [0, 1]
        else:
            s[i] = [s[i-1][0]+s[i-2][0], s[i-1][1]+s[i-2][1]]
            
    print(s[n][0], s[n][1]) 