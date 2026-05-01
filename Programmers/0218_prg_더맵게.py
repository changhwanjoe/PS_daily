# 힙 사용법 공부 
'''
import heapq
heap =[]
elm = 1
heapq.heappush(heap,elm)
heapq.heappop(heap)
]
'''
import heapq
def solution1(scoville, K): # 효율성 테스트 실패 
    count =0
    trig = False
    while True:
        if len(scoville) ==1 and scoville[0] >=K:
            return count
        elif len(scoville)<2:return -1
        else: 
            scoville.sort(reverse=True)
            first,second = scoville.pop(),scoville.pop()
            if first>=K: return count
            scoville.append(first+second*2)
            count +=1 

import heapq
def solution(scoville,K):
    answer = 0
    heapq.heapify(scoville) 
    while True:
        min1 = heapq.heappop(scoville)
        if min1 >=K : break
        elif len(scoville) == 0: 
            answer = -1 
            break
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville,min1+min2*2)
        answer +=1 
    return answer
scoville, K = [1, 2, 3, 9, 10, 12],	7

print(solution(scoville, K))
