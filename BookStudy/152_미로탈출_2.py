from collections import deque

N, M = map(int,input().split())
graph = []
for i in range(M):
    graph.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    count = 0
    visited= []
    while q:
        tx,ty = q.popleft()
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]         
            if nx < 0 or nx>=N or ny <0 or ny >= M:
                continue
            if graph[nx][ny] == 0:
                continue 
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[tx][ty] +1 
                q.append((nx,ny))
    return graph[N-1][M-1]
print(bfs(0,0))



#def bfs(int v, start, visited):
    
