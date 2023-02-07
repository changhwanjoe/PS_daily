import collections
import heapq
from typing import List

def networkDelayTime(self, times : List[List[int]], N: int, K: int) -> int:
    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w)) # v = time, w = node

    Q = [(0, K)] #(time, node)

    dist = collections.defaultdict(int)

    while Q:
        time, node = heapq.heappop(Q) # node = K
        if node not in dist: #-> not in key
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))
