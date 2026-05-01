# 필요하면 * -> 10 # -> 12 로 바꿀것, 0->11 
# 원본 훼손 해도 문제없음

def solution(numbers, hand):
    only_l = [1,4,7]
    only_r = [3,6,9]
    index = 1
    dic = {}
    for i in range(4):
        for j in range(3):
            dic[index] = (i,j)
            index+=1
    lx,ly = 3,0 # 왼손가락 좌표 
    rx,ry = 3,2 # 오른손가락 좌표
    answer = ''
    for num in numbers:
        if num==0: num =11
        px,py = dic[num] 
        if num in only_l : # 왼손만
            lx,ly = px,py # num 좌표 
            result = 'L'
        elif num in only_r:
            rx,ry = px,py
            result = 'R'
        else: # 3,6,9
            result = distance(lx,ly,rx,ry,px,py,hand)
            if result == 'L' : lx,ly = px,py # num 좌표 
            elif result == 'R': rx,ry = px,py
        answer += result 
    return answer

def distance(lx,ly,rx,ry, px,py, hand):
    l_dis = abs(lx-px)+abs(ly-py)
    r_dis = abs(rx-px)+abs(ry-py)
    if l_dis > r_dis : return 'R'
    elif l_dis < r_dis: return 'L'
    else : # 같을때
        if hand == 'right': return 'R'
        elif hand == 'left' : return 'L'
        
if __name__=="__main__":
    numbers,hand = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"
    numbers,hand = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left", 
    print(solution(numbers, hand))