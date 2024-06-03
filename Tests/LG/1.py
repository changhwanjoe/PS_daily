import sys
readl = sys.stdin.readline
 
def sol1(T):
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
    
                if HP<=0 or HP >10**13+1: #용사 체력이 최대보다 크면 반복문 끊어줌. 시간 초과 이슈 
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

def sol2(T):    
    for _ in range(T):
        N = int(readl())
    
        D = list(map(int,readl().split()))
        S = list(readl())[:-1]
        R = list(map(int,readl().split()))
    
        HP = 1 + D[-1]
    
        idx = N-2
    
        while idx>=0:
            if S[idx]=='+': # 더하기 주문서 
                HP += - R[idx]
                if HP <=0:
                    HP = 1
            else:
                if HP % R[idx] != 0:
                    HP = HP // R[idx] +1
                else:
                    HP = HP // R[idx]
    
            HP += D[idx]
    
            idx += -1
    
        print(HP)


if __name__=="__main__":
    T = int(readl())
    sol2(T)
