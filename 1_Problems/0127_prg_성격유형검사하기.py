# zip 사용법
def solution(survey, choices):
    scoring = [-3, -2, -1, 0, 1, 2, 3]
    answer = ''
    label = ["RT","CF","JM","AN"]
    score = [0,0,0,0]
    for sur, choice in zip(survey, choices):
        a, b = sur[0], sur[1]
        for ind,elm in enumerate(label):
            if a in elm :
                if sur ==elm: score[ind] += scoring[choice - 1]
                else: score[ind] -= scoring[choice - 1]
                break
    for sc,lb in zip(score,label):
        if sc>0: answer+=lb[1]
        else : answer +=lb[0]
    return answer

if __name__=="__main__":
    survey,choices= ["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]
    print(solution(survey, choices))
    