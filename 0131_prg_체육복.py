def solution1(n, lost, reserve): # 모범답안 
    s = set(lost) & set(reserve)
    r = set(reserve) - s
    l = set(lost) - s
    for x in sorted(r) : 
        if x - 1 in l:
            l.remove(x-1)
        elif x+1 in l:
            l.remove(x+1)
    return n-len(l)


def solution2(n, lost, reserve):
    answer = 0
    student = [1]*n
    for no in lost:
        student[no-1]-=1
    for yes in reserve:
        student[yes-1]+=1
    
    for ind,elm in enumerate(student):
        if elm ==0:
            if ind <n-1:
                if student[ind+1]>=2:
                    student[ind+1]-=1
                    student[ind]+=1
                    continue
            if ind>0:
                if student[ind-1]>=2:
                    student[ind-1]-=1
                    student[ind]+=1
                    continue

    for elm in student:
        if elm >=1:
            answer +=1
    return answer



if __name__=="__main__":
    n,lost,reserve = 5,[2, 4],[1, 3, 5]
    n,lost,reserve = 5,[2, 4],[3]
    n,lost,reserve = 3,[3],[1]
    print(solution(n, lost, reserve))
