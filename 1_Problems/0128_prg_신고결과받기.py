# 자료구조를 먼저 정하고 시작
## for i in dictionary 로 접근할때 i에 Key 가 return 됨
## answer[list.index(i)] index로 번지수 접근하는법

#solution

from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    
    reportee_list = defaultdict(list) 
    mailing_list = defaultdict(int)
    
    for elm in report:
        reporter, reportee = elm.split()
        if reporter not in reportee_list[reportee]:
            reportee_list[reportee].append(reporter)
        else:
            continue
    for key,value in reportee_list.items():
        if len(value) >=k:
            for reportee in value:
                mailing_list[reportee] +=1 
    for id in id_list:
        answer.append(mailing_list[id])
    return answer

if __name__ == "__main__":
    id_list,report,k= ["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2
    print(solution(id_list, report, k))