from collections import deque
n,m = map(int, input().split())
graph  = []
for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]


q =deque([start])

visited = [False] * n

q.append((x,y))

while q:
    x_t, y_t = q.popleft()
    visited[(x_t, y_t)] = True

    for i in range(4):
        new_x = x_t + dx[i] 
        new_y = y_t + dy[i]
        if new_x>=0 and new_x<n and new_y >=0 and new_y<M:
            q.append((new_x,new_y))
              



