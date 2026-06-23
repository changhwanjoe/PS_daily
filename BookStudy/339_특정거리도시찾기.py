from collections import deque

N,M,K,X = map(int,input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
	a,b = map(int,input().split())
	graph[a].append(b)

distance = [-1] * (N+1)

q = deque()
q.append(X)
distance[X] = 0

while q:
	v = q.popleft()
	for w in graph[v]:
		if distance[w] == -1:
			distance[w] = distance[v] +1
		else:
			distance[w] = min(distance[w], distance[v]+1)
		q.append(w)

for i, dis in enumerate(distance):
	if dis == K:
		print(i)

			




# from itertools import permutations
# from itertools import combinations

# li = [1,2,3,4]

# #print(list(permutations(li,2)))
# print(list(combinations(li,2)))

# import heapq

# q = []
# heapq.heappush(q,(1,2))

# heapq.heappush(q,(3,2))

# heapq.heappush(q,(0,2))

# a = heapq.heappop(q)
# print(a)