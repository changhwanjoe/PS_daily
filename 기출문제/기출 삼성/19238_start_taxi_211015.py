from collections import defaultdict, deque
import sys
#sys.stdin = open("C:\\Users\\chjoe\\OneDrive\\Documents\\GitHub\\SWexpert\\4_ss_python\\input.txt", "r")
sys.stdin = open("19238_input.txt", "r")
input = sys.stdin.readline
N, M, fuel = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if ground[i][j]==1:
            ground[i][j] = -1

r, c = map(int, input().split()) # row, column of start taxi
client = [list(map(int, input().split())) for _ in range(M)] # r, c, d_r,d_c

des = [[0 for _ in range(N)] for _ in range(N)]
for l in range(M):
    cy, cx = client[l][0]-1, client[l][1]-1
    dy, dx = client[l][2]-1, client[l][3]-1
    ground[cy][cx] = l+1
    des[dy][dx] = l+1

#start_r, start_c, des_r, des_c
start_v = [r, c]
dy = [-1, 0 ,0 ,1]
dx = [0, -1, 1, 0]

def bfs1(s_y,s_x): # finding client
    global N,M, fuel
    visited = []
    q = deque()
    visited.append([s_y,s_x])
    q.append([s_y,s_x])
    
    if M == 0:
        return -2
    while q :
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<= ny < N and 0<= nx <N and [ny,nx] not in visited:
                if ground[ny][nx] == -1 :
                    visited.append([ny,nx])
                    continue
                elif ground[ny][nx]> 0:
                    M-=1
                    client_num = ground[ny][nx]
                    ground[ny][nx] = 0
                    res = bfs2(client_num, ny, nx)
                    return
                else:
                    visited.append([ny,nx])
                    q.append([ny,nx])
        fuel -= 1
        if fuel == 0:
            return -1

def bfs2(num, s_y, s_x):
    global N, M,fuel
    discovered = []
    q = deque()
    discovered.append([s_y, s_x])
    cnt = 0
    q.append([ny,nx])
    while fuel:
        while q :
            cnt+=1
            y,x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0<= ny < N and 0<= nx <N:
                    if ground[ny][nx] == -1 :
                        discovered.append([ny,nx])
                    elif des[ny][nx] == num:
                        des[ny][nx] = 0
                        fuel += cnt *2
                        return 1
                    else:
                        discovered.append([ny, nx])
                        q.append([ny, nx])
    return -1

print(bfs1(r-1,c-1))

#
#
#
#
#
# def bfs1 (start_v):
#      global N
#     global ground
#     global des
#     global init_fuel
#
#     car_y, car_x = start_v[0]-1, start_v[1]-1
#     if ground[car_y][car_x]>=1:
#         return car_y,car_x,ground[car_y][car_y]
#     q = deque()
#     q.append([car_y, car_x])
#     discovered = [[car_y, car_x]]
#     new_pos = []
#     dy = [-1, 0, 0, 1]
#     dx = [0, -1, 1, 0]
#
#     while q:
#         if init_fuel == 0:
#             return None
#         vy, vx = q.popleft()
#         init_fuel -= 1
#
#         for i in range(4):
#             ny = vy + dy[i]
#             nx = vx + dx[i]
#             if ny >= 0 and ny < N and nx >= 0 and nx < N:
#                 if [ny,nx] in discovered:
#                     continue
#                 elif ground[ny][nx] == -1:
#                     discovered.append([ny,nx])
#                     continue
#                 elif ground[ny][nx] > 0: # client eixst
#                     return ny, nx,ground[ny][nx]
#                 else:
#                     discovered.append([ny,nx])
#                     q.append([ny, nx])
#
# def bf2(start_v, number):
#     q = deque()
#     v_y, v_x = start_v
#     q.append([v_y, v_x])
#     discovered = [v_y, v_x]
#     dy = [-1, 0, 0, 1]
#     dx = [0, -1, 1, 0]
#     cnt = 0
#     global init_fuel
#     while q:
#         if init_fuel ==0:
#             return None
#         v_x, v_y = q.popleft()
#         cnt += 1
#         init_fuel -= 1
#         for _ in range(4):
#             ny = v_y + dy[i]
#             nx = v_x + dx[i]
#             if ny >= 0 and ny < N and nx >= 0 and nx < N:
#                 if ground[ny][nx] == -1 :
#                     continue
#                 elif des[ny][nx] == number:
#                     des[ny][nx] = 0
#                     init_fuel += cnt *2
#                     return init_fuel
#
# for i in range(M):
#     if init_fuel == 0:
#         result = 0
#         break
#     else:
#         bfs_res = bfs1([r,c])
#         if bfs_res != None:
#             res = bf2(bfs_res[0],bfs_res[1])
# print(res)
#
# # def bfs2(start_v):
# #     q = [start_v]
# #     discovered = [start_v]
# #     while q:
# #         v = q.pop(0)
# #         for w in grpah[v]:
# #             if w not in discovered:
# #                 discovered.append(w)
# #                 q.append(w)
#
#
#
