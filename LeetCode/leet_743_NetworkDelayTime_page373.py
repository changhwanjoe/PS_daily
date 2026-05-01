import collections
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)

        #그래프의 인접 리스트 구성
        for u, v, w in times:
            graph[u].append((v, w))

        #큐 변수 : [(소요시간, 접점)]
        Q = [(0, K)] #첫 노드 소요시간 0, 시작 노드 K
        dist = collections.defaultdict(int)

        #우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]: #pop된 node에 붙어있는 모든 노드들에 대해, (노드번호v, weight)를 pop
                    alt = time + w # time은 출발점부터 node까지 걸린시간 + node 부터 v까지 걸리는 t
                    heapq.heappush(Q, (alt, v))

        if len(dist) == N:
            return max(dist.values())
        return -1

#times = [[2,1,1],[2,3,1],[3,4,1]]
times2 = [[3, 1, 5], [3, 2, 2], [2, 1, 2],[3, 4, 1],[4, 5, 1],[5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 1, 1]]
N = 8
K = 3

s = Solution()
result = s.networkDelayTime(times2, N, K)
print(result)
