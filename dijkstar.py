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
    distance[start] = 0 

    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1 
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)
for i in range(1,n+1):
    if distance[i] == INF : 
        print("INF")
    else:
        print(distance)



INF = int(1e9)
import heapq
from collections import deque
graph = [[] for i in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c)) 
    # a 에서 b 가는 비용 c

# distance =[0,INF,INF,INF]
# q = ()

def dijkstra(start):

    q = []
    distance[start] = 0 # visited
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
           
        for w_node, w_cost in graph[now]:
            cost = dist + w_cost
            if distance[w_node] > cost:
                heapq.heappush(q, (cost,w_node))
