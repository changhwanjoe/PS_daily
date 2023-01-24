# 코딩테스트 연습> 해시> 완주하지 못한 선수


def solution(participant, completion):
    d = {}
    for x in participant:
        d[x] = d.get(x,0) + 1 # d 딕셔너리 안에 x 가 있으면 value 값을, 없으면 0 뱉음
    for x in completion:
        d[x] -= 1 
    answer_ = [k for k,v in d.items() if v >0 ] 
    answer = answer_[0]
    return answer

if __name__== "__main__":
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]

    print(solution(participant,completion))