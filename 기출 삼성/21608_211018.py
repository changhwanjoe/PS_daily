# 211019 참고 : https://hillier.tistory.com/76

from collections import defaultdict, deque
import sys

input = sys.stdin.readline
dy = [-1, 0, 1, 0]
dx = [0 , -1, 0, 1]
student = defaultdict(list)
student_order= deque()
N = int(input())

visited = [[0]*N for _ in range(N)]

for i in range(N*N):
    li = list(map(int, input().split()))
    #student[i] = [li[1],li[2],li[3],li[4]]
    student[li[0]] = li[1:]
    student_order.append(li[0])

#ground = [[0 for _ in range(N) for _ in range(N)]]
ground = [[0]*N for _ in range(N)]
cnt = 0
def cnt_favorite(y, x, std_num):
    favorite_cnt = 0
    empty_cnt = 0
    global N
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if ny>=0 and ny<N and nx >=0 and nx<N:
            if ground[ny][nx] in student[std_num]:
                favorite_cnt += 1
            elif ground[ny][nx] == 0:
                empty_cnt += 1
    return favorite_cnt, empty_cnt

max_favorite_xy = [[]]
max_empty_xy = [[]]

for num in range(1, N*N+1):
    student_num = student_order.popleft()
    max_favorite_cnt = -1
    max_empty_cnt = -1
    for i in range(N):
        for j in range(N):
            if ground[i][j]!=0:
                continue
            favorite, empty = cnt_favorite(i, j, student_num)
            if favorite > max_favorite_cnt or (max_favorite_cnt == favorite and max_empty_cnt < empty):
                max_favorite_xy = [i, j]
                max_favorite_cnt = favorite
                max_empty_cnt = empty
    ground[max_favorite_xy[0]][max_favorite_xy[1]] = student_num

result = 0

for i in range(N):
    for j in range(N):
        seat_num = ground[i][j]
        favorite_sum = 0
        for k in range(4):
            ny = dy[k] + i
            nx = dx[k] + j
            if 0 <= ny < N and 0<= nx <N:
                if ground[ny][nx] in student[seat_num] :
                    favorite_sum +=1
        if favorite_sum!=0 :
            result += 10**(favorite_sum-1)

print(result)


