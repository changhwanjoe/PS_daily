import heapq
INF = int(1e9)

n,m = map(int, input().split())

start = int(input())
graph = [[] for _ in range(n+1)]
# 최단거리 1차원 테이블 초기화
dist = [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    # a에서 b번으로 가는 비용이  C 일때
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    visited = []
    
    for destination, distance in graph[start]: 
        heapq.heappush(q, (distance, destination))


    while q :
        dist, now = heapq.heappop()
        if dist


