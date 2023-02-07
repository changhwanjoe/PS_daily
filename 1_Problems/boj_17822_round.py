import sys

sys.stdin = open("input.txt",'r')

def turn_reverse_clock(i, k):
    for ni in range(i,N+1,i): #from i to N, ++i
        for _ in range(k):
            plate[ni-1].append(plate[ni-1].pop(0))

def turn_clock(i, k):
    for ni in range(i,N+1,i):
        for _ in range(k):
            plate[ni-1].insert(0,plate[ni-1].pop())

def find_same_num():
def remove_num(pos):
def find_avr_plus_minus_1():

N, M, T = map(int,input().split())
#plate = [list(map(int, input().split())) for _ in range(N)]
plate = [list(map(int, input().split())) for _ in range(N)] # the string list in input.split() changed in to int list

for _ in range(T):
    i,d,k= map(int,input().split())
    if d: #counter clock
        turn_reverse_clock(i,k)
    else:
        turn_clock(i,k)

    pos = find_same_num()
    if pos : # if there is same number
        remove_num(pos)
    else : # No same number
        find_avr_plus_minus_1()

print(sum(map(sum, plate)))

