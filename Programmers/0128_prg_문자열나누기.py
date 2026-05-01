def solution(s):
    answer = 0
    remain = s
    while True:
        remain = solver(remain)
        answer+=1  
        if remain =="":
            break
    return answer

def solver(s):
    x=s[0]
    c_same,c_diff = 0,0
    for ind,ch in enumerate(s):
        if ch ==x:
            c_same +=1
        else: c_diff +=1 
        if c_same==c_diff:
            return s[ind+1:]
    return ""
