from collections import deque
import sys
INF = 1e9 # 무한을 의미하는 10억
sys.stdin = open("16236_input.txt", "r")
input = sys.stdin.readline


n = int(input())
array = []
for i in range(n):
    array.append(list(map(int,input().split())))

# 아기 상어의 현재 크기 변수와 현재 위치 변수
now_size = 2
now_x, now_y = 0,0

# 아기상어의시작 위치 찾은 뒤에 그 위치 아무것도 없다고 처리
for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = i,j
            array[now_x][now_y] = 0
dx = [-1,0,1,0] #상 우 하 좌
dy = [0,1,0,-1]

# 모든 위치 까지 최단거리만 계산하는 BFS 함수
def bfs():
    # 값이 -1 이면 도달할 수 없다는 의미
    dist = [[-1]*n for _ in range(n)]
    # 시작 위치는 도달이 가능하다고 보며 거리는 0 
    q = deque([(now_x,now_y)])
    dist[now_x][now_y] = 0
    while q : 
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<= nx and nx<n and 0<= ny and ny<n:
                # 자신의 크기보다 작거나, 같은 경우에 지나갈 수 있음
                if dist[nx][ny] == -1 and array[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] +1 
                    q.append((nx,ny))
    return dist

# 최단 거리 테이블이 주어졌을때 먹을 물고기를 찾는 함수
def find(dist) : 
    x,y = 0,0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            # 도달이 가능하면서 먹을 수 있는 물고기 일때
            if dist[i][j] != -1 and 1<=array[i][j] and array[i][j] < now_size:
                # 가장 가까운 물고리 1마리만 선택
                if dist[i][j] <min_dist:
                    x,y = i, j
                    min_dist = dist[i][j]

    if min_dist == INF : # 먹을수 있는 물고기 없을경우
        return None
    else: 
        return x,y,min_dist # 먹을 물고기와 위치와 최단거리

result = 0
ate = 0

while True:
    # 먹을 수 있는 물고기의 위치 찾기
    value = find(bfs())
    # 먹을 수 있는 물고기가 없는 경우, 현재까지 움직인 거리 출력
    if value == None:
        print(result)
        break
    else :
        # 현재 위치 갱신 및 이동거리 변경
        now_x, now_y = value[0],value[1]
        result += value[2]
        # 먹은 위치에 아무것도 없도록 처리
        array[now_x][now_y] = 0
        ate +=1

        # 자신의 현재 크기 이상으로 먹은경우, 크기 증가
        if ate>=now_size :
            now_size+=1
            ate = 0
