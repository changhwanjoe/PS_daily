from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    reporting_list = defaultdict(list)
    banned_list = defaultdict(int)
    
    for elm in report:
        temp = elm.split()
        reporter, bad_man = temp[0],temp[1]

        if reporter == bad_man:
            continue

        if not reporting_list[reporter] : # reporter not in dic --> report first time
            reporting_list[reporter] = [bad_man]
        else : 
            if bad_man in reporting_list[reporter]:
                continue
            else:
                reporting_list[reporter] +=[bad_man]
        
        if banned_list[bad_man] == 0 :
            banned_list[bad_man] = 1
        else:
            banned_list[bad_man] +=1 
    answer = [0 for _ in range(len(id_list))]
    #print(banned_list)
    #print([li for li in banned_list.keys()], k)
    reported_list = [li for li in banned_list.keys() if banned_list[li] >= k]
    #print(f'banned_list :  {banned_list} ,\n dic : {reporting_list}, \nreported_list = {reported_list}')
    for ind, name in enumerate(id_list):
        for have in reporting_list[name]:
            if have in reported_list:
                answer[ind] +=1 

    
    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k=2
id_list2 = ["con", "ryan"]
report2 = ["ryan con", "ryan con", "ryan con", "ryan con"]

#print( solution(id_list2, report2, k))
print(solution(id_list,report,k))