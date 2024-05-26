import sys
readl = sys.stdin.readline
 
T = int(readl())
 
for _ in range(T):
    N = int(readl())
 
    D = list(map(int,readl().split()))
    S = list(readl())[:-1]
    R = list(map(int,readl().split()))
 
    right = 10**13 + 1 # 최대 데미지, 용사가 무조건 승리
    left = 1 # 최소값
    mid = (left + right) //2
 
    while left != right:
        HP = mid
 
        for n in range(N):
            HP += -D[n]
 
            if HP<=0 or HP >10**13+1:
                break
 
            if S[n] == '+':
                HP += R[n]
            else:
                HP *= R[n]
 
        if HP <= 0:
            left = mid +1
 
        else:
            right =mid
 
        mid = (left + right)//2
 
    print(right)  