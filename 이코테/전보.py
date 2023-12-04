from collections import deque
import heapq
N,M,C = map(int,input().split())
graph =[0]*30000 
for i in range(M):
    x, y, z = map(int,input().split())
    graph[x].append((y,z))


INF = int(1e9)
distance = [INF]*(N+1)

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    
    while q :
        dist,now =  heapq.heappop(q)
        if distance[now] < dist:
            continue
        else:
            for w in graph[now]:
                next_node, next_cost = w[0], w[1],
                cost = next_cost + dist
                if cost < distance[next_node]:
                    distance[next_node] = cost 
                    heapq.heappush(q,(cost,next_node))

dijkstra(C)

count = 0 
max_distance =  0 
for d in distance:
    if d != INF:
        count +=1 
        max_distance = max(d, max_distance)

print(count-1, max_distance)




