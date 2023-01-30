# 배운점 : string.replace("대상","new string", count) Count 는 몇번 바꿀지 정하는것. 
# 1이면 여러번 있어도 한번만 바꾼다. 
# "@"워드를 공백으로 처리해서 length 0 으로 만든게 포인트
def solution(babbling):    
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

def solution2(babbling): # 모범답안
    answer = 0
    for msg in babbling:
        msg = msg.replace("aya","@",1)
        msg = msg.replace("ye", "@",1)
        msg = msg.replace("woo", "@",1)
        msg = msg.replace("ma", "@",1)
        msg = msg.replace("@","") # 이부분 좋음 
        if len(msg) ==0: 
            answer+=1
    return answer

     

if __name__=="__main__":
    babbling = ["aya", "yee", "u", "maa", "wyeoo"]
    print(solution(babbling))
    babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
    