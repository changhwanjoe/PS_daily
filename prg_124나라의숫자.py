def solution(n):
    answer = ''
    li = ["4","1","2"]
    while True:
        a = n//3 # 몫
        b= n % 3  # 나머지
        
        if a >0 and b==0: # 3진수 일때
            a-=1 
        answer =li[b]+answer
        if a==0: break
        n=a
    return answer