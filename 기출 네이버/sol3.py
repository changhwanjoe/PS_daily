def solution(letters, k):
    from itertools import combinations
    answer = ''
    li = [''.join(i) for i in list(combinations(letters, k))]
    li.sort()
    answer = li[-1]
    return answer