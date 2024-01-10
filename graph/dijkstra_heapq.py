import heapq
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

def dijkstra(start):
    q = []
    
    heapq.heappush(q, (0,start)) # 시작 노드로 가기 위한 최단 경로는 0으로 설정
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        if distance[now] < dist: # 이미 처리된 적 있는 노드라면 무시
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                                
dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
