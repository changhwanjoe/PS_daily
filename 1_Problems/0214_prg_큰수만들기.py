# 숫자가 문자열로 되어있을때
# 한자리의 대소비교는 숫자와 같음 
# but 2자 이상일때는 앞자리 먼저 비교 

def solution(number, k):
    collected = []
    for i, num in enumerate(number):
        while len(collected) >0 and collected[-1] < num and k>0:
        # 빼낼 갯수가 남아있으면서 마지막 갯수
            collected.pop()
            k-=1
        if k==0:
            collected+=list(number[i:])
            break
        collected.append(num)
    collected = collected[:-k] if k >0 else collected
    answer = ''.join(collected)
    return answer

number,k = "1924",	2
number,k = "1231234",  3
number,k = "4177252841", 4
print(solution(number,k))