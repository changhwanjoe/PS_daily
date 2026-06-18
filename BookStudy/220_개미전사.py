N = int(input())
array = list(map(int,input().split()))


d = [-1]*(N)
d[0] = array[0]
d[1] = max(array[1],array[0])

for i in range(2,N):
    d[i] = max(array[i]+d[i-2], d[i-1])

print(d[N-1])