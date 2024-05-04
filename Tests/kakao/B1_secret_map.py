import collections
import sys
# 필요한것
# 1.  십진수- 이진수 진수변환
# 2. bit masking . *
sys.stdin = open("secret_map.txt", "r")
input = sys.stdin.readline

N = int(input())
arr1 = map(int,input().split())
arr2 = map(int,input().split())
arr3 = []
for a,b in zip(arr1,arr2):
    c= bin(a | b)[2:]
    res = ""
    res2 = ""
    for elm in c:
        if elm=="1":
            res+="#"
        elif elm == "0":
            res+=" "
    d = bin(a|b)[2:].zfill(N).replace("1","#").replace("0"," ")
    res2+=d

    print(f"res2 = {res2}" )
    print(f"res = {res}")
