import re
def solution(s):
    for i in range(1, len(s)//2+1):
        reList = re.sub('(\w{%i})' %i, '\g<1> ',s).split()
        print(reList)
        count = 1
        result = []
        for j in range(len(reList)):
            if j == len(reList) - 1 :
                if count == 1:
                    continue
                else:
                    result.append(count)
                    result.append(reList[j])
            if reList[j] == reList[j+1] : 
                count+=1
            else:
                if count ==1 :
                    continue
                else:
                    result.append(count)
                    result.append(reList[j])
                    count = 1
            print(result)
        # for j in range(0,len(s)-)
        # s[:1]
    answer = 0
    return answer

print(solution('aabbaccc'))