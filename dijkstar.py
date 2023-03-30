import heapq
INF = int(1e9)

n,m = map(int, input().split())

start = int(input())
graph = [[] for _ in range(n+1)]
# 최단거리 1차원 테이블 초기화
distance = [INF]*(n+1)

# 

for _ in range(m):
    a,b,c = map(int, input().split())
    # a에서 b번으로 가는 비용이  C 일때
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    dist[start] = 0 

    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1 
            if cost < distance[i[0]]:
                heapq.heappush(q,(cost,i[1]))



