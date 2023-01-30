def solution(babbling):
    answer = 0
    babbling_list = ["aya", "ye", "woo", "ma"]
    answer =0 
    for word in babbling:
        trig = True
        for babb in babbling_list:
            word = word.replace(babb,"@")
        
        for ch in word:
            if ch!="@": 
                trig= False
                break
        if trig : answer+=1 
         
    return answer


if __name__=="__main__":
    babbling = ["aya", "yee", "u", "maa", "wyeoo"]
    print(solution(babbling))
    babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
    