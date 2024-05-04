# 21610 비바라기 문제
# https://velog.io/@qweadzs/BOJ-21610-%EB%A7%88%EB%B2%95%EC%82%AC-%EC%83%81%EC%96%B4%EC%99%80-%EB%B9%84%EB%B0%94%EB%9D%BC%EA%B8%B0Python 
# -> 잘하는듯
from collections import defaultdict
from collections import deque
import sys

def move_rain(dir, dist):
    global n
    size = len(cloud)
    for _ in range(size):
        x, y = cloud.popleft()
        nx = (x + dx[dir] * dist) % n # (중요)
        # new_x 
        ny = (y + dy[dir] * dist) % n
        # new(y)
        if 0 > nx:
            nx += n 
        if 0 > ny:
            ny += n
        cloud.append((nx, ny))
        # 구름이 사라진 자리를 표시
        visited[nx][ny] = True
        graph[nx][ny] += 1


def dup():
    while cloud:
        # 대각선 검사
        x, y = cloud.popleft()
        for i in range(1, 8, 2): # 1,3, 5, 
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > 0:
                graph[x][y] += 1 # 비 추가

if __name__== "__main__":
    input = sys.stdin.readline 
    n, m= map(int, input().split())
    A = [] # water
    B = [] # cloud existance

    graph = [list(map(int, input().split())) for _ in range(n)]
    # for i in range(n):
    #     A.append(list(map(int, input().split())))
    dir_move = [list(map(int, input().split())) for _ in range(m)]

    #    ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 
    dx = [0,-1,-1, -1 ,0, 1, 1, 1]
    dy=  [-1,-1,0, 1,  1, 1, 0,-1]
    # d = direction 
    # s  = distance
    # if rain = A[r][c] + 1
    # cloud[r][c]
    # water copy = 

    # inital cloud
    cloud = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]
    # change cloud into deque
    cloud = deque(cloud)

    for dir, dist in dir_move:
        visited = [[False] * n for _ in range(n)] # 매 턴 visited 초기화
  
        # 1. 구름 이동 후 비 내리기
        move_rain(dir - 1, dist)
        # 2. 물 복사
        dup()
        # 3. 구름 생성
        for i in range(n):
            for j in range(n):
                if graph[i][j] >= 2 and not visited[i][j]:
                    cloud.append((i, j))
                    graph[i][j] -= 2
    answer = 0
    for i in range(n):
        for j in range(n):
            answer += graph[i][j]
    print(answer)

    sol = solution()
    print(sol)
