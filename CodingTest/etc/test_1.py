import sys

def input_data() :
	readl = sys.stdin.readline
	N = int(readl()) 
	D = list(map(int, readl().split()))
	return N, D


def Solve():
	sol = -30001
	sum = 0
	for i in range(0,N) :
		if sum>=0:
			sum += D[i]
		else :
			sum = D[i]
		if sol < sum: 
			sol=sum
	return sol

#입력받는 부분
N, D = input_data()
sol = Solve()
print(sol)#출력하는 부분
