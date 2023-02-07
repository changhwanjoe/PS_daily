def solution(word):
    from itertools import product
    repeat_num = 0
    whole_list = []
    for repeat_num in range(1,6):
        li = [''.join(i) for i in list(product([ 'A', 'E', 'I', 'O', 'U'], repeat=repeat_num))]
        whole_list+=li

    whole_list.sort()
    answer = 0
    #answer = whole_list.find()
    answer = whole_list.index(word)
    return answer+1

#print(solution("AAAAE")+1)