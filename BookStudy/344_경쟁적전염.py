from collections import deque
import heapq

n,k = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

s,tx,ty = map(int,input().split())

temp = [[0] * n for _ in range(n)]

q = []

dx = [-1,1,0,0]
dy = [0,0,1,-1]


for i in range(n):
    for j in range(n):
        if graph[i][j] >0:
            heapq.heappush(q, (graph[i][j], i, j))


new_q = []
count = 0
def run():
    global count 
    while q:
        prior, x,y = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] ==0:
                    graph[nx][ny] = prior
                    heapq.heappush(new_q, (prior, nx, ny))
    count += 1
    if graph[tx-1][ty-1] > 0:
        return graph[tx-1][ty-1]      
    if count >= s:
        return 0     


for i in range(s):
    result = run()
    print(result)