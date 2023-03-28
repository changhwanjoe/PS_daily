from collections import deque

INF = 1e9

n = int(input())
array = []
for i in range(n):
    array.append(list(map(int,input().split())))

now_size = 2 
now_x, now_y = 0,0

for i in range(n):
    for j in range(n):
        if array[n][j] ==9:
            now_x,now_y = i,j
            array[n][j] = 0
        

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs():
    dist = [[-1] *n for _ in range(n)]
    q= deque([(now_x,now_y)])
    dist[now_x][now_y]=0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny= y+dy[i]
            if 0<=nx<n and 0<=ny <n:
                if 
                if 0<array[nx][ny]<now_size:

                 