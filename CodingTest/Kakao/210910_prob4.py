lion_list = [0 for _ in range(11)]
result = []
global max_score
max_score = 0 

def solution(n, info):
    ms = max_score
    dfs(n,info, 0, lion_list,ms)
    print(result)
    answer = []
    print(max_score)
    if max_score == 0:
        answer = -1
    else:
        answer = max_score

    return answer


def calculate_score(peach_shot, lion_shot):
    peach = 0
    lion = 0
    for i in range(11):
        if peach_shot[i] == 0 and lion_shot[i] == 0:
            continue
        elif (peach_shot[i]-lion_shot[i])>=0 :
            peach+= 10-i
        else:
            lion+= 10-i
    diff = lion - peach
    if diff <=0:
        return -1 
    else :
        return diff

def dfs(n,info, index, path,ms):
    if n<0:
        return 
    elif n == 0:
        score = calculate_score(info, lion_list)
        
        if score > ms: 
            ms = score
            result= (path.copy())
        return 

    for i in range(index, len(lion_list)):
        path[i]+=1 
        dfs(n-1,info, i, path,ms)
        path[i]-=1

n= 5
info = [2,1,1,1,0,0,0,0,0,0,0]	
#result = [0,2,2,0,1,0,0,0,0,0,0]
print(solution(n,info))