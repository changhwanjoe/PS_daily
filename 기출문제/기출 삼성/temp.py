# import sys

# sys.stdin = open("temp_input.txt", "r")
# input = sys.stdin.readline
# m=4


# sys.stdin = open("temp_input.txt", "r")
# input = sys.stdin.readline

# dir = [[] for _ in range(m)]
# idx = -1
# for i in range(4*m):
#     if i % 4 == 0:
#         idx += 1
#     dir[idx].append(list(map(int, input().split())))

# dirl = [[] for _ in range(m)]

# for i in range(m):
#     for j in range(4):
#         dirl[i][j].append(list(map(int, input().split())))

n=5
ret = [[0]*n for _ in range(n)]
n_ret = [[0]*n for _ in range(n)]

count= 0
for r in range(n):
    for c in range(n):
        ret[r][c] = count
        count +=1
def print_mat(mat):
    for r in range(n):
        print(mat[r])
print_mat(ret)
print()
for r in range(0,n):
    for c in range(0,n):
        n_ret[c][n-r-1] = ret[r][c]

print_mat(n_ret)
