import sys

def InputData():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    A = list(map(int, readl().split()))
    B = list(map(int, readl().split()))

    return N, M, A, B

first = 1 
def Find(start):
    global B, first
    
    if first == 1:
        first = 0
        B.sort()
        B = list(map(lambda x:x-B[0], B))

    P = A[start:start+M]
    P.sort()
    
    P = list(map(lambda x: x-P[0], P))
    return B == P

def Solve():
    sol = 0
    for i in range(N-M+1):
        sol += Find(i)
    return sol
N, M, A, B = InputData()
# 코드를 작성하세요
sol = Solve()

# 출력
print(sol)
