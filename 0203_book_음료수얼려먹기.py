from collections import deque


def solution(N,M,graph):
    answer = 0
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] ==0:
                bfs(graph,i,j)
                answer +=1 
    return answer 

def dfs(graph,x,y):
    dx = [-1, 1, 0, 0]
    dy = [0 ,0 ,-1,1 ]
    q = deque()
    q.append((x))

def bfs(graph, x,y):   
    dx = [-1, 1, 0, 0]
    dy = [0 ,0 ,-1,1 ]
    stack = deque()
    stack.append((x,y))
    graph[x][y] = 1
    while stack:
        tx,ty = stack.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] ==0:
                stack.append((nx,ny))
                graph[nx][ny]= 1

#N,M = map(int,input().split())
#graph = list(map(int, input().split()) for _ in range(N)) 
N,M = 4,5
graph = [[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]
print(solution(N,M,graph))