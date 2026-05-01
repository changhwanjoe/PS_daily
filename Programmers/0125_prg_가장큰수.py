# 배울점 : sort 에 key 넣는법. 람다 활용법, 내림차순 정리 

def solution(numbers):
    answer = ''
    numbers = [str(x) for x in numbers]
    numbers.sort(key = lambda x: (x*4)[:4],reverse=True) # input 의 최대가 1000이므로 4자리 숫자로 만듬. 
    # 그다음 앞에서부터 4개 글자만 끊음, 정렬시에는 큰숫자부터(reverse)
    # 3-> 3333 / 34->3434 / 342 -> 3423
    answer = ''.join(numbers)
    if numbers[0] == '0': return '0'
    return answer

numbers = [6, 10, 2]
numbers = [3, 30, 34, 5, 9]
print(solution(numbers))