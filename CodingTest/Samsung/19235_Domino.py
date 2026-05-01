import sys
import collections
import heapq
sys.stdin = open("19235_input.txt", "r")
input = sys.stdin.readline

#x : 행 y : 열

N = int(input()) # N :  블록을 놓은 횟수
block_num = [list(map(int, input().split())) for i in range(N)]

print("N", N, type(N))
print("bock", block_num,type(block_num))
t, x, y = block_num[0]
print("block[0]",t,x,y, type(t))

score = 0
blue_tile_num = 0
green_board = [[0 for _ in range(4)] for _ in range(6)]
blue_board  = [[0 for _ in range(4)] for _ in range(6)]


def solutions():
    for i in range(N):
        t, x, y = block_num[i]
        if t ==1 :

            pass
        elif t ==2 :
            pass
        elif t ==3 :
            pass


        print(score)
        print(blue_tile_num)

def put_g_block(g_board, t, x, y):
    exist = []
    if t == 1:
        for j in range(5,-1,-1):
            if g_board[j][y]!= 0:
                heapq.heappush(exist,[j,y])

        tx, ty = heapq.heappop(exist)
        x, y = tx - 1, ty





    return g_board

def put_b_block(b_board, t, x, y):





def row_delete():
    pass

def column_delete():
    pass