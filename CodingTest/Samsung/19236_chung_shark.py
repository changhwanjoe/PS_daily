import sys
from copy import deepcopy
from collections import defaultdict

sys.stdin = open("19236_input.txt", "r")
input = sys.stdin.readline

impor copy


#map1  =[[0 for _ in range(4)] for _ in range(4)]

fish = [[] for _ in range(16)]
a =[[] for _ in range(4)]

for i in range(4):
    temp = []
    temp = list(map(int, input().split()))
    for j in range(0,7,2): # j = 0, 2,4,6
        fish_num = temp[j] -1
        fish_heading = temp[j+1] -1
        fish[fish_num] = [i, j//2] # fish[i] = [x,y,h]
        a[i].append([fish_num, fish_heading])#  [j//2] = fish_num                 # map[x][y] = i  i = 0, 1,2,3

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

ans = 0
d, cnt = a[0][0][1], a[0][0][0]+1  # 5 , 7
fish[a[0][0][0]] = [] #fish[6] = []
a[0][0] = []

dfs(0, 0, d, cnt)
print(ans)
#direction
# 0  1   2   3  4  5   6  7
# 상 좌상 좌 좌하 하 우하 우 우상
# 반시계-> 디렉션 방향 +

# map1[x][y] = 물고기 넘버
# fish[i] = [x,y,h]
# shark = [x,y,h]

def dfs(x, y, d, cnt):
    global ans
    global fish, a
    move_fish()

    if not -1 < tx< 4 or -1 < tx < 4:
        return score

    else:
        score += fishnum + 1
        sharkhead = fishhead

    while True :
        nx = tx + dx[sharkhead]
        ny = ty + dy[sharkhead]
        if not -1 < tx < 4 or -1 < tx < 4: # 맵을 넘기면,
'''=======
def solution(tx, ty, th, map1, score):

    while True:
        if not -1 < tx < 4 or -1 < tx < 4:
>>>>>>> Stashed changes'''
            return max()


        if map1[nx][ny] > -1: # 맵에 물고기 있으면
            score += map1[nx][ny] + 1
            new_fish_head = fish[map1[nx][ny]][2]
            fish[map1[nx][ny]] = 0
            map1[nx][ny] = -1 # 맵에 상어 있으면 -1
            map1[tx][ty] = -2  # 맵에 아무것도 없으면 -2
            shark = [nx, ny, new_fish_head]

            dfs(nx, ny, map1[nx][ny], )

        elif map1[tx][ty] == -2 : #맵에 물고기 없으면



        else:

        tx = nx
        ty = ny

        shark = [tx, ty, th]


def move_fish(sx,sy):
    global fish
    global a

    for i in range(16):
        if fish[i] != []: # if fish exist
            x, y = fish[i] # x, y heading
            h = a[x][y][1]
            for m in range(8):
                t = (h + m) % 8
                nx = x + dx[t]
                ny = y + dy[t]
                if -1 < nx < 4 and -1 < ny < 4 and nx != sx and ny != sy : #a[nx][ny] != -1: # not shark // shark  = -1
                    if a[nx][ny] :  # fish exist
                        next_fish = a[nx][ny][0]
                        next_fish_head =  a[nx][ny][1]
                        temp_h = fish[next_fish][1] # 그 자리에 있던 물고기 머리방향
                        fish[i] = [nx, ny, t]
                        fish[nf] = [x, y, nh]
                        map1[nx][ny] = i
                        map1[x][y] = nf
                        break
                    else:  # no fish
                        map1[nx][ny] = i
                        map1[x][y] = -2 # // no fish
                        fish[i] = [nx, ny, t]
                        break

         # 다음좌표에 물고기가 있고, 이동할수 있다면,
            li = []
            s1 = solution(tx + dx[th], ty + dy[th], th, map1, score)
            s2 = solution(tx + 2*dx[th], ty + 2*dy[th], th, map1, score)
            s3 = solution(tx + 3*dx[th], ty + 3*dy[th], th, map1, score)
            li.extend([s1,s2,s3])
            score = max(li)
            return score
        else:
            return score


print(solution(0,0,5,map1, 0))
dfs(0, 0, 6, 5) # 맵에서, 다음 상어의 위차와, 그 자리 물고기번호, 그자리 물고기 방향을 넣어줌.













