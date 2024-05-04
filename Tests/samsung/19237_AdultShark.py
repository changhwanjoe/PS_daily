import sys
import collections
from collections import deque
import itertools

import heapq

sys.stdin = open("19237_input.txt", "r")
input = sys.stdin.readline

#dx[0] ,dy[0] : 위

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] #dx[0], dy[0] = 상 하 좌 우
n, m, k = map(int, input().split()) # n = 격자, m = M 마리 상어, K= 피냄새 

sharks = [[0, 0] for _ in range(m)] # [[0,0], [0,0],[0,0]]

board = [] # 

shark_map = [[] for _ in range(m)]
smell_map = collections.defaultdict(list)
smell_map = [[] for _ in range(m)]
shark = {}
my_smell = []

for i in range(n):
    list1 = list(map(int, input().split())) # shark map
    board.append(list1) #board [0] = [0,0,0,3] board[1] board[2]
    for j in range(n):
        if list1[j]: # not 0 -> if shark exist
            shark_map[list1[j]-1].extend([i,j]) # shark_map[i] => i 번 상어의 좌표 x,y  
            board[i][j] = [list1[j]-1, k] # board = smell map[0] -> 상어번호, k 

direction = list(map(int, input().split())) # 상어 향하고 있는 방향 1,2,3,4, 상하좌우
for h in range(len(direction)):
    direction[h] -= 1

dirlist= [[]]
for j in range(4):
    for i in range(n):
        dirlist[j].append(list(map(int, input().split())))
                # 상0       하1        좌2        우3
#dirlist[0] = [[2 3 1 4],[4 1 2 3],[3 4 2 1],[4 3 1 2]]
#dirlist = [list(map(int,input().split())) for _ in range(4*m)] # 우선순위 리스트 dir[
#
#
# for i in sharkmaep.keys():
#     if len(sharkmaep[i])>2:
#         print(i)
#         print(sharkmaep.values())
#print(dirlist)

def where_to_go(sharknum:int, current_heading:int):
    return dirlist[sharknum][current_heading-1]

# 1번 상어만 격자에 남게 되기까지 걸리는 시간을 출력한다.
def soltution (n, m, k ,board, smell, list1):
    keepgoing = True
    count = 0
    while keepgoing :
        for i in range(m): # 모든 상어들에 대해
            x, y = sharks[i] # n번 샤크의 x,y 좌표
            if x>0 and y>0: # 살아있는 상어
                hdg = direction[i] #머리 방향 # 0 1 2 3 상 하 좌 우
                prio_list= []
                smell_count = 0
                for l in range(4):
                    prio_list = dirlist[i][hdg]
                    new_hdg = prio_list[l]

                    nx = x + dx[new_hdg-1]
                    ny = y + dy[new_hdg-1]
                    if smell_count == 4 :
                        sx,sy = my_smell.popleft()
                        sharks[i] = [sx, sy]
                        shark_map[(x, y)] = []
                        temp = []
                        temp = shark_map.get((sx,sy))
                        temp.append(i)
                        shark_map[(sx, sy)] = temp
                        a= sx - x
                        b= sy - y
                        if (a,b) == (1,0):
                            next_current_hdg = 1

                        elif (a, b) == (-1, 0):
                            next_current_hdg = 0
                        elif (a, b) == (0, 1):
                            next_current_hdg = 3
                        elif (a, b) == (0, -1):
                            next_current_hdg = 2
                        # if a,b = 1,0 :아래  0,1 오 -1,0 위 0,-1 왼
                        direction[i] = next_current_hdg

                        pass
                    else:
                        if -1 < nx < n and -1 < ny < n :# 다음 좌표가 맵을 넘어가지 않는다면,
                            if smell_map[(nx,ny)] != []: #냄새가 있다?
                                smell_count +=1
                                if smell_map[(nx,ny)][1] == i :# 내 냄새다?
                                    my_smell.append((nx,ny))
                                    continue
                                else:
                                    continue
                            else : # 냄새가 없다?
                                sharks[i] = [nx,ny]
                                shark_map[(x, y)] = []
                                temp = []
                                temp = shark_map.get((nx, ny))
                                temp.append(i)
                                shark_map[(nx, ny)] = temp
                                a = nx - x
                                b = ny - y
                                if (a, b) == (1, 0):
                                    next_current_hdg = 1

                                elif (a, b) == (-1, 0):
                                    next_current_hdg = 0
                                elif (a, b) == (0, 1):
                                    next_current_hdg = 3
                                elif (a, b) == (0, -1):
                                    next_current_hdg = 2
                                # if a,b = 1,0 :아래  0,1 오 -1,0 위 0,-1 왼

                                direction[i] = next_current_hdg

                        else:
                            smell_count += 1
            else: #죽어있는 상어에 대해
                pass

        ## 다 돌았다면 죽은애 있는지
        for temp_li in shark_map.values():
            if len(temp_li)>1:
                temp_li.sort()
                min_i = temp_li.popleft()
                shark_map[shark[min_i]] = [min_i]
                for oo in temp_li:
                    shark[oo] = [-1, -1]

        for i in smell_map.keys():
            if smell_map[(i)] != []:
                a, b = smell_map[(i)]
                if a == 1:  # 냄새 쿨 빠지면, 공집합으로 바꾸기
                    smell_map[(i)] = []
                else:
                    smell_map[(i)] = [a - 1, b]
        # 냄새남기기
        for i in range(m): # 모든 상어들에 대해
            x, y = sharks[i] # n번 샤크의 x,y 좌표
            if x>0 and y>0:
                smell_map[(x,y)] = [k,i]

        count += 1

        temp_ho = 0
        for i in range(m):
            x, y = sharks[i]
            if x>0 and y>0:
                temp_ho +=1
        if temp_ho == 1:
            return count

        elif count >1000:
            return -1

    print("count", count)


soltution (n, m, k ,board, smell_map, list1)