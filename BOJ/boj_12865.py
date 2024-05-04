# kanp sack problem
# https://claude-u.tistory.com/208
first_row = input()

N, K = int(first_row.split()[0]), int(first_row.split()[1])
W = []
V = []
for _ in range(N):
    sec_row = input()
    W.append(int(sec_row.split()[0]))
    V.append(int(sec_row.split()[1]))

for