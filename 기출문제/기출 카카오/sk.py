from collections import deque, defaultdict
from itertools import permutations
dic = defaultdict()

def solution(goods):
    answer =[[] for _ in range(len(goods))]

    def find_distinct(word,length):
        dis_li = []
        for i in range(len(word)+1-length):
            temp =""
            for j in range(length):
                temp+=word[i+j]
                #print(temp)
            dis_li.append(temp)
        return dis_li
    
    for ind,elm in enumerate(goods):
        flag = True
        while flag:
            for k in range(1,len(elm)+1):
                dis_li = find_distinct(elm,k)
                for dis_word in dis_li:
                    if dis_word in answer[ind]:
                        continue
                    cnt = 0 
                    for words in goods:
                        if words == elm:
                            continue
                        else:
                            if dis_word not in words:
                                cnt +=1 
                            else:
                                break
                    if cnt == len(goods)-1:
                        answer[ind].append(dis_word)
                        flag = False
                if flag == False:
                    break
            if k == len(elm):
                answer[ind].append("None")
                break
    #print(answer)
    new_answer = []
    for answer_list in answer:
        
        answer_list.sort()#.join(" ")
        new_answer.append(" ".join(answer_list))
#        print(answer_list)
        # print(answer_list)
        # # for elm in answer_list:
        # #     t+=elm
        #     answer[ind]=
            
        #0, pencil = 
        #1, cilicon 
        #2, contarbase 
        #3, picurlist
    
    
    return new_answer

goods = ["abcdeabcd","cdabe","abce","bcdeab"]
goods = ["abcdeabcd","cdabe","abce","bcdeab"]
#goods = ["pencil","cilicon","contrabase","picturelist"]
print(solution(goods))

