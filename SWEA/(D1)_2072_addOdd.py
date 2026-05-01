a=int(input())
for i in range(1,a+1):
    k=0
    b=list(map(int,input().split(" ")))
    for j in range(0,10):
        if b[j]%2==1:
            k=k+b[j]
    print("#%d %d"%(i,k))
