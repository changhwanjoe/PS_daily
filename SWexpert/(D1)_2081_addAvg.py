a=int(input())
for i in range(1,a+1):
    k=0
    b=list(map(int,input().split(" ")))
    for j in range(0,10) : 
        k = k+b[j]
    k1 = round(k/10)
    print("#%d %d"%(i,k1))
