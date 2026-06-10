'''
Problem number : Boj 11611
Date : 2021. 08.28
Problem Src : https://www.acmicpc.net/problem/21611
Solution Src : https://imksh.com/64
'''
import sys

input = sys.stdin.readline

N, M = map(int,input().split())

plate = [list(map(int, input().split())) for _ in range(N)]
mag = [list(map(int, input().split())) for _ in range(M)]


direction = [[0,0],[0,-1],[0,1],[-1,0],[1,0]] #(정지)상1 하2 좌3 우4
broken_marble = [0,0,0] #파괴한 구슬의 수 (1, ,2, 3 )
indexing = {}



def first_phase(): # 마법으로 폭발
    pass
def second_phase(): # 연속된 번호 폭발
    pass
def thrid_pahse(): # 구슬 번호 변화
    pass

for i in range(1, s+1):
    # d방향으로 s만큼 깨기
    nx, ny = x+dx[d]*i, y+dy[d]*i
    board[nx][ny] = 0

if __name__=="__main__":
    pass