# 코딩테스트 연습> 해시> 완주하지 못한 선수
# d.get 함수

def solution(participant, completion):
    d = {}
    for x in participant:
        d[x] = d.get(x,0) + 1 # d.get(x,0): return value, or 0 if x not in d's keys 
    for x in completion:
        d[x] -= 1 
    #did not finish
    dnf = [k for k,v in d.items() if v >0 ] # d.items(): return key, value
    answer = dnf[0]
    return answer

def sol2(participant, completion): # not optimzed answer
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]

if __name__== "__main__":
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]

    print(solution(participant,completion))