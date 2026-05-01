"""
다익스트라 최단경로 알고리즘 연습
- 구현 1: 인접 리스트 + 최소 힙 (기본)
- 구현 2: 구조 분해(unpacking) 활용 버전
"""
import heapq
from collections import deque

INF = int(1e9)

n, m = map(int, input().split())

start = int(input())
graph = [[] for _ in range(n + 1)]
# 최단거리 1차원 테이블 초기화
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # a에서 b번으로 가는 비용이 c일 때
    graph[a].append((b, c))


# ===== 구현 1 =====

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]          # [FIX] dist + 1 → dist + i[1] (가중치 반영)
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])             # [FIX] distance → distance[i] (개별 값 출력)


# ===== 구현 2: 구조 분해(unpacking) 활용 =====

distance2 = [INF] * (n + 1)


def dijkstra2(start):
    q = []
    distance2[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance2[now] < dist:
            continue

        for w_node, w_cost in graph[now]:
            cost = dist + w_cost
            if distance2[w_node] > cost:
                distance2[w_node] = cost    # [FIX] distance 갱신 누락 수정
                heapq.heappush(q, (cost, w_node))
