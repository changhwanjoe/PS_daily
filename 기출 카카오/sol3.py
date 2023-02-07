def solution(info, query):
    answer = []
    finder_list = []
    employee_list = []
    query_num = len(query)
    participant_num = len(info)

    for j in range(query_num):
        finder_list.append(query[j].replace('and','').split())

    for i in range(participant_num):
        employee_list.append(info[i].split())
    for i in range(query_num):
        count = 0
        for j in range(participant_num):
            temp = []
            tf = None
            a= employee_list[j]
            b= finder_list[i]
            temp = (char_comparison(a, b))
            #print(temp)
            if not False in temp:
                tf = True
                count +=1
        answer.append(count)

    return answer

def char_comparison(a,b):
    temp_in_func = []
    for i in range(len(b)-1):
        if b[i]== '-':
            temp_in_func.append(True)
        else:
            if b[i]==a[i]:
                temp_in_func.append(True)
            else :
                temp_in_func.append(False)
                return temp_in_func

    if (int(a[-1]) >= int(b[-1])):
        temp_in_func.append(True)
    else:
        temp_in_func.append(False)

    return temp_in_func