import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

n, m = map(int,input().split()) # 노드의 개수, 간선의 개수
start = int(input()) # 시작 노드 번호 입력
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF]*(n+1) # 최단 거리 테이블 초기화

for _ in range(m): 
    a, b, c = map(int, input().split())
    graph[a].append((b,c)) # a => b로 가는 비용이 c
    
def get_smalles_node(): # 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드 번호 반환
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] =j[1]
    
    for i in range(n - 1):
        now = get_smalles_node()
        visited[now] = True
        
        for j in graph[now]:
            cost = distance[now] + j[1]
            
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                
dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
