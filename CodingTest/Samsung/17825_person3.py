#https://empty-cloud.tistory.com/66
import sys
movements = list(map(int, sys.stdin.readline().split()))
path_info = [
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0],
    [10, 13, 16, 19, 25],
    [20, 22, 24, 25],
    [30, 28, 27, 26, 25],
    [25, 30, 35, 40, 0]
]
# [i-th path, j-th block]
piece_positions = [[0, 0], [0, 0], [0, 0], [0, 0]]
piece_scores = [0, 0, 0, 0]
answer = 0


def dfs(idx):
    # termination condition
    if idx == 10:
        global answer
        answer = max(answer, sum(piece_scores))
        return answer

    # how many steps are going to be moved 각 턴마다 말이 움직일 횟수를 가져온다. (24~25번째 줄)
    move = movements[idx]

    for i in range(4):
        # current piece position
        cur_path = piece_positions[i][0]
        cur_block = piece_positions[i][1]

        # if current piece finished the game 현재 위치를 구하고, 만약 현재 위치가 도착지점이라면 다음 말로 넘어간다.(= 다음 말을 이동시킨다.) (32~34번째 줄)
        if cur_block == len(path_info[cur_path]) - 1:
            continue

        next_path = cur_path # 각 말마다 다음 위치를 구하고, 그다음 위치가 만약 각 코너와 중앙이라면, 이동할 경로의 번호와 위치를 바꿔준다. (36~56번째 줄)
        next_block = cur_block + move
        # change path at the corner
        if cur_path == 0:
            if next_block == 5:
                next_path = 1
                next_block = 0
            elif next_block == 10:
                next_path = 2
                next_block = 0
            elif next_block == 15:
                next_path = 3
                next_block = 0
            elif next_block == 20:
                next_path = 4
                next_block = 3
        # change path at the center point
        elif cur_path < 4:
            if next_block >= len(path_info[cur_path]) - 1:
                next_path = 4
                next_block -= len(path_info[cur_path]) - 1

        # limit block to the last block of the path #만약 말의 다음 위치가 도착을 넘어간다면, 도착에서 이동을 마친다. (58~60번째 줄)
        if next_block >= len(path_info[next_path]):
            next_block = len(path_info[next_path]) - 1

        # without the first & last block #시작과 도착을 제외하고, 만약 현재 말의 다음 위치에 이미 다른 말이 있다면, 다음 말로 넘어간다.(= 다음 말을 이동시킨다.) (62~66번째 줄)
        if path_info[next_path][next_block] != 0:
            # if next step is already taken
            if [next_path, next_block] in piece_positions:
                continue

        # move piece and update information #모든 조건을 통과하고 난 후, 말을 이동시킨다. (68~71번째 줄)
        piece_positions[i][0] = next_path
        piece_positions[i][1] = next_block
        piece_scores[i] += path_info[next_path][next_block]

        dfs(idx + 1) #DFS를 통해 모든 경우를 재귀적으로 탐색한다. (73번째 줄)

        # reset piece and information #이동시킨 말을 다시 원래 위치로 되돌린다. (75~78번째 줄)
        piece_positions[i][0] = cur_path
        piece_positions[i][1] = cur_block
        piece_scores[i] -= path_info[next_path][next_block]


dfs(0)
print(answer)
