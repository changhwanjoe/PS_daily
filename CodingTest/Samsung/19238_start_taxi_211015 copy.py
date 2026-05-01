from collections import deque
import sys
import copy
sys.stdin = open("19238_input.txt", "r")
input = sys.stdin.readline

N, M, fuel = map(int, input().split())
client_graph = [[0]*N for _ in range(N)]
desti_graph = [[0]*N for _ in range(N)]
graph =[[0]*N for _ in range(N)]

client = []
destination = []


graph = [list(map(int,input().split())) for _ in range(N)]
client_graph = copy.deepcopy(graph)
destin_graph= copy.deepcopy(graph)
sx,sy = map(int,input().split)

mapping = [list(map(int,input().split())) for _ in range(M)]
for i in range(M):
    cr,cc,dr,dc=mapping[i]
    client_graph[cr][cc] = -i
    destin_graph[cr][cc] = -i

for j in range(M):
    graph[i]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]    


def bfs(start_x,start_y):
    global client_graph
    global fuel 
    q = deque()
    q.append((start_x,start_y))
    visited =[(start_x,start_y)]
    count = 0
    while q:
        if fuel ==0 :
            return False,0,0,0
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if (nx,ny) in visited: continue
            elif 0<=nx<N and 0<=ny<N and client_graph[nx][ny]!= 1 :
                if client_graph[nx][ny] <0: 
                    num = client_graph[nx][ny]
                    client_graph[nx][ny] = 0
                    return True, nx, ny, num
                else:
                    q.append((nx,ny))
                    visited.append((nx,ny)) 
        fuel -=1 



def client_bfs(start_v):
    if client_graph[nx][ny]<0:
        target = client_graph[nx][ny]
        client_graph[nx][ny] = 0
        return True

