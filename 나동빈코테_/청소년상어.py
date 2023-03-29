from collections import deque

import copy

array =[[None]*4 for _ in range(4)]


for i in range(4):
    data = list(map(int,input().split()))
    for j in range(4):
        array[i][j] = [data[i*2],data[j*2+1]-1]

dx = [-1,-1, 0, 1,1,1,0,-1]
dy = [0, -1,-1,-1,0,1,1, 1]

def turn_left(d):
    return (d+1) % 8

result = 0

# 현재 배열에서 특정한 번호의 물고기 위치 찾기
def find_fish(array,index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i, j)
    return None

# 모든 물고기를 회전 및 이동 시키는 함수
def move_all_fishes(array,now_x,now_y):
    for i in range(1,17):
        position = find_fish(array,i)
        if position != None:
            x,y = position[0],position[1]
            direction = position[2]
            
            nx, ny = x + dx[d] + y+dy[d]
                 