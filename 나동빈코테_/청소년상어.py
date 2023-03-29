from collections import deque

import copy

array =[[None]*4 for _ in range(4)]

for i in range(4):
    data = list(map(int,input().split()))
    for j in range(4):
        array[i][j] = [data[i*2],data[j*2+1]-1]