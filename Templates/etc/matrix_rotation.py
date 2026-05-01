"""
행렬 회전(rotate), 전치(transpose), 달팽이(snail) 구현

사용법:
    python matrix_rotation.py
"""

N = 5
count = 1
graph = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        graph[i][j] = count
        count += 1


def print_grid(grid):
    """2차원 배열을 포맷팅하여 출력"""
    n = len(grid)
    for i in range(n):
        li = [format(elm, '02') for elm in grid[i]]
        print(li)
    print("\n")


def rotated(grid):
    """90도 시계방향 회전"""
    n = len(grid)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n - i - 1] = grid[i][j]
    return result


def transpose(grid):
    """전치 행렬 (행↔열 교환)"""
    n = len(grid)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][i] = grid[i][j]       # [FIX] 동시 swap 로직 오류 → 단순 대입
    return result


def snail(n):
    """달팽이 배열 생성"""
    result = [[0] * n for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    d = 3
    count = 1
    x, y = 0, 0
    while count <= n * n:
        result[x][y] = count
        nx, ny = x + dx[d], y + dy[d]
        if (0 <= nx < n) and (0 <= ny < n) and result[nx][ny] == 0:
            x, y = nx, ny
        else:
            d = (d + 1) % 4
            x, y = x + dx[d], y + dy[d]
        count += 1
    return result


if __name__ == "__main__":
    print_grid(graph)

    rot = rotated(graph)
    print("\nrotated")
    print_grid(rot)

    sn = snail(N)
    print("\n snail")
    print_grid(sn)

    tr = transpose(graph)
    print("\n transpose")
    print_grid(tr)
