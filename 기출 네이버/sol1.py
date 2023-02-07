def solution(S, pattern):
    count = 0
    #print(f'{S} hi {pattern}')
    for ind,letter in enumerate(S):
        if letter in pattern:
            tf = check(S[ind:ind+len(pattern)],pattern)
            if tf : count +=1
        else:
            continue
    answer = count
#    answer = -1
    return answer

def check(word, pattern):
    from itertools import permutations
    if pattern in [''.join(i) for i in list(permutations(word,len(word)))]:
        return True
    else:
        return False

# S ="tegsornamwaresomran"
# pattern = "ransom"

# res = solution(S,pattern)
# print(res)