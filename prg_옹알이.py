def solution(babbling):
    answer = 0
    for word in babbling:
        if check(word):
            answer+=1 
    return answer

def check(word):
    babbling_list = ["aya", "ye", "woo", "ma"]
    while len(word)>0:
        for elm in babbling_list:
            if word.startswith(elm):
                word = word[len(elm):]
                babbling_list.remove(elm)
                break
        



if __name__=="__main__":
    babbling = ["aya", "yee", "u", "maa", "wyeoo"]
    babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
    solution(babbling)