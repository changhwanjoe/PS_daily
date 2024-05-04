from collections import defaultdict, deque
import sys
sys.stdin = open("C:\\Users\\chjoe\\OneDrive\\Documents\\GitHub\\SWexpert\\4_ss_python\\input.txt", "r")
input = sys.stdin.readline
N, M, init_fuel = map(int,input().split())
ground = [list(map(int,input().split())) for _ in range(N)]
r,c = map(int, input().split())
client = [list(map(int, input().split()))]
#start_r, start_c, des_r, des_c

def graph(pos):
    dy = [-1, 0 , 0, 1]
    dx = [0, -1, 1, 0]
    global N
    new_pos = []
    for i in range(4):
        ny = pos[0] + dy[i]
        nx = pos[1] + dx[i]
        if ny >=0 and ny<N and nx>=0 and nx<N:
            new_pos.append([ny,nx])
    return new_pos

def bfs1 (start_v):
    y,x = start_v
    q = deque()
    q.append(start_v)
    discovered = [start_v]
    while q :
        v = q.popleft()
        for w in graph(v):
            if w not in discovered:
                y,x = w
                if ground[y][x] ==1 : # if wall
                    discovered.append(w)
                elif client[w] == 1:
                    discovered.append(w)
                    break
                else:
                    q.append(w)
                    discovered.append(w)
    return 
print(bfs1([client[0][0],client[0][1]]))


# def bfs2(start_v):
#     q = [start_v]
#     discovered = [start_v]
#     while q:
#         v = q.pop(0)
#         for w in grpah[v]:
#             if w not in discovered:
#                 discovered.append(w)
#                 q.append(w)


        
