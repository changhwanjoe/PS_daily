'''최단경로를 찾는 문제로,
least_distance_func((structure (x,y): car_position, structure (x,y): guest_position) -> int :
만 만들면 해결될듯?

'''
import sys
import collections
from collections import deque
import heapq

#### main###
sys.stdin = open("19238_input.txt", "r")
input = sys.stdin.readline

N, M, fuel = map(int, input().split())
env_map = []
for i in range(N):
    env_map.append(list(map(int, input().split())))
    for j in range(N):
        if env_map[i][j] == 1:
            env_map[i][j] = -1

driver_x, driver_y = map(int, input().split())
des_map = [[] for _ in range(M + 1)] # d = [[],[],[],[]]

for i in range(M): # 0번부터 M-1 번까지.
    psg_x, psg_y, des_x, des_y = map(int, input().split())
    env_map[psg_x - 1][psg_y - 1] = i + 1 #1번부터 M번까지 #pasger 위치에 passenger 번호 넣음
    des_map[i + 1] = [des_x - 1, des_y - 1]

# N, M, fuel, env_map, des_map, des_x, ,des_y, driver_x, driver_y, psg_x , psg_y ,
# def bfs1  입력 : 드라이버 x,y 좌표로부터 가장 가까운 승객을 찾음.
# def bfs2 -> 입력 : 승객의 x,y 를 받아서, 승객으로부터 목적지를 찾음. 승객 지우고, 목적지도 지워야함.

dx =[-1, 0, 0, 1] # dx[0] = left dx[1] = right
dy =[0, -1, 1, 0] # dy[2] = UP  dy[3] = down
from collections import deque
def bfs(start_x, start_y) : # finding client
    t_x, t_y = start_x, start_y

    visited = []
    q = deque()
    q.append((t_x, t_y))
    while q :
        v_x, v_y= q.popleft()
        if (v_x,v_y) not in visited:
            visited.append((v_x, v_y))
            for i in range(4):
                nx = v_x + dx[i]
                ny = v_y + dy[i]
                if 0<=nx<N and 0<=ny<N and env_map[nx][ny] != -1 :
                    if env_map[nx][ny] >= 1:
                        client_num = env_map[nx][ny]
                        env_map[nx][ny] = 0
                        print(f"client_num {client_num} just hopped in on {nx},{ny}")
                        return nx, ny, client_num
                    else:
                        q.append((nx, ny))

def bfs2(start_x,start_y,client_num):
    des_x, des_y = des_map[client_num]
    visited = []
    q = deque()
    q. append((start_x,start_y))
    while q:
        t_x,t_y = q.popleft()
        if (t_x,t_y) not in visited:
            visited.append((t_x,t_y))
            for i in range(4):
                nx = t_x + dx[i]
                ny = t_y + dy[i]
                if 0<=nx<N and 0<= ny <N and env_map[nx][ny] != -1 :
                    if (nx, ny) == (des_x, des_y):
                        print(f"client {client_num} arrived at {des_x},{des_y}")
                        return des_x, des_y
                    else:
                        q.append((nx, ny))
li = []
des_x,des_y = 6,5
while True :
    nx,ny, client_num = bfs(des_x,des_y)
    des_x,des_y=bfs2(nx,ny,client_num)
    li.append((des_x,des_y))
    if len(li) >= M :
        break
