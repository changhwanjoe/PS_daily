# stack queue --> deque
def solution2(ingredient): # 모범답안. Stack의 맨위 4개만 보고 1231 일때 pop 시키면 훨씬 쉽다
    answer = 0
    stack = []
    for elm in ingredient:
        stack.append(elm)
        if len(stack) >=4:
            if stack[len(stack)-4:] == [1,2,3,1]: # 이부분 핵심. 
                for _ in range(4): stack.pop()
                answer+=1
    return answer
    

from collections import deque
def solution(ingredient): # 내 답안. 
    answer = 0
    prev = 0
    d = deque()
    for elm in ingredient:
        if elm ==1 :
            if len(d)==0:
                d.append(elm)
            else: # 데크 스택에 뭔가 있는경우 
                if d[-1]== 3:
                    for _ in range(3):
                        d.pop()
                    answer+=1
                else: d.append(elm)
        else: # 2 or 3인경우
            if len(d) == 0:
                continue
            elif elm ==2 : 
                if d[-1]== 1:
                    d.append(elm)
                else : #2 or 3
                    d = deque() # clear stack
            elif elm ==3 :
                if d[-1] == 2:
                    d.append(elm)
                else : d = deque() # clear stack
    return answer

def clear_stack(d):
    while True:
        a = d.pop()
        if a==1:break


if __name__=="__main__":
    ingredient= [2, 1, 1, 2, 3, 1, 2, 3, 1]
    print(solution(ingredient))
    ingredient= [1, 3, 2, 1, 2, 1, 3, 1, 2]
    print(solution(ingredient))
