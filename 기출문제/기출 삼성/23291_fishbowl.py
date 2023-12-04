# https://devlibrary00108.tistory.com/663
#좀 무식하게 푼 느낌이 없잖아 있습니다.
# 달팽이 거꾸로 파고들면서 그렸습니다.
#빈칸은 -1로 표기 빈칸 없을때와 빈칸이 있을 떄 1열로 펼치는 순서가 다릅니다.

import sys
input = sys.stdin.readline
from collections import deque


# 달팽이를 만든다. 시작좌표는
def make_snail():
    row, col = n, n
    if n**2 - N >= n:
        col -= 1
    matrix = [[0] * col for _ in range(row)]
    q = deque()
    q.append((row - 1, col - 1, 0))
    blank_cnt = row * col - N
    start = N - 1
    while q:
        x, y, d = q.popleft()
        matrix[x][y] = arr[start]
        if blank_cnt:
            matrix[x][y] = -1
        for i in range(d, d + 4):
            i %= 4
            nx, ny = x + delta[i][0], y + delta[i][1]
            if 0 <= nx < row and 0 <= ny < col and not matrix[nx][ny]:
                q.append((nx, ny, i))
                if blank_cnt:
                    blank_cnt -= 1
                else:
                    start -= 1
                break
    return matrix


# 최솟값들에 대해 1더해준다.
def engage_minimum():
    min_v = min(arr)
    for i in range(N):
        if arr[i] == min_v:
            arr[i] += 1


def spread(matrix):
    row = len(matrix)
    col = len(matrix[0])
    new_matrix = [[0] * col for _ in range(row)]
    if matrix[-1][-1] == -1:
        row -= 1
        a, b = row - 1, row
        if matrix[a][0] != -1 and matrix[b][0] != -1:
            if matrix[a][0] < matrix[b][0]:
                a, b = b, a
            move = (matrix[a][0] - matrix[b][0]) // 5
            new_matrix[a][0] -= move
            new_matrix[b][0] += move
        for y in range(col):
            if matrix[row][y] == -1:
                break
            for dy in (1, -1):
                ny = y + dy
                if 0 <= ny < col and matrix[row][ny] != -1:
                    if matrix[row][y] - matrix[row][ny] < 5:
                        continue
                    move = (matrix[row][y] - matrix[row][ny]) // 5
                    new_matrix[row][ny] += move
                    new_matrix[row][y] -= move
    for x in range(row):
        for y in range(col):
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col:
                    if matrix[x][y] - matrix[nx][ny] < 5:
                        continue
                    move = (matrix[x][y] - matrix[nx][ny]) // 5
                    new_matrix[nx][ny] += move
                    new_matrix[x][y] -= move
    if matrix[-1][-1] == -1:
        row += 1
    for i in range(row):
        for j in range(col):
            matrix[i][j] += new_matrix[i][j]
    return matrix


# 달팽이인데 오른족 아래 빈칸 상태면 왼쪽 위부터 행을 순서대로 읽는다.
# 완전한 정사각형이면 왼쪽 아래부터 위로 열을 순대로 읽는다.
def make_arr(matrix):
    row = len(matrix)
    col = len(matrix[0])
    ret = []
    if matrix[-1][-1] == -1:
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == -1:
                    continue
                ret.append(matrix[i][j])
    else:
        for i in range(col):
            for j in range(row - 1, -1, -1):
                ret.append(matrix[j][i])
    return ret


# 행 4개에 분배하기. 배열 4등분 해서 뒤집은 3번째, 2번째, 뒤집은 1번째, 4번째 순.
def make_four_row(arr):
    new_matrix = []
    new_matrix.append(arr[pivot * 2:pivot * 3][::-1])
    new_matrix.append(arr[pivot:pivot * 2])
    new_matrix.append(arr[:pivot][::-1])
    new_matrix.append(arr[pivot * 3:])
    return new_matrix


N, K = map(int, input().split())
arr = list(map(int, input().split()))
pivot = N // 4
for i in range(2, 11):
    if i**2 >= N:
        n = i
        break

delta = ((0, -1), (-1, 0), (0, 1), (1, 0))

answer = 0
while max(arr) - min(arr) > K:
    # 1. 최솟값들에 대해 1씩 넣어준다.
    engage_minimum()
    # 2. 왼쪽을 중앙으로 시작해서 달팽이.
    # N보다 큰 제곱수의 2차원 배열을 만든 후 남는 칸수만큼 오른쪽에서 offset을 준 뒤 달팽이 하며 감아 들어가면 됨.
    matrix = make_snail()
    # 3. 달팽이에서 인접칸 검사 (a - b) // 5만큼 분배. 동시 분배.
    matrix = spread(matrix)
    # 4. 펼치는건 왼쪽 아래부터 위로
    arr = make_arr(matrix)
    # 첫 N // 4는 뒤집어서 2행, 다음 N// 4는 그대로 1행, 그다음 N // 4는 뒤집어서 0행 마지막 N // 4는 그대로 3행.
    matrix = make_four_row(arr)
    # 6. 물고기 분배 한번 더.
    matrix = spread(matrix)
    # 7. 1열부터 펼치면 3행부터 거꾸로 올라가며 펼치면 됨.
    arr = make_arr(matrix)
    answer += 1
print(answer)
