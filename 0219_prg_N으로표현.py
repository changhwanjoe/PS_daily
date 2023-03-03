def solution(N, number):
    answer = 0
    if N == number:
        return 1
    # s에는 집합이 8개 들어있고
    # 각 x 에는 5 55 555 등이 들어있음
    s= [set() for _ in range(8)] # set() *8 로 하면 안됨
    for i, x in enumerate(s,start=1):  # i는 1부터 시작 
        x.add(int(str(N)*i)) # 셋에 추가 5 55 555 5555

    for i in range(1, len(s)):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1+op2)
                    s[i].add(op1-op2)
                    s[i].add(op1*op2)
                    if op2!= 0:
                        s[i].add(op1//op2)
        if number in s[i]: # 주어진 인자가 집합 안에 포함되어 있으면 
            answer = i+1
            break
        else:
            answer = -1 


    # 1개 : 5 
    # 2개 : 55 / 10 0 25 1 
    # 3개 : 555 / 55 +-/* 5 / 5 5 5 
    # 

    return answer