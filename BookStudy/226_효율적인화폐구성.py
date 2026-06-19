N,M = map(int,input().split())
coin = []
for i in range(N):
    coin.append(int(input()))
print(coin)

coin.sort()
print(coin)