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
    count = 0
    heapq.heapify(scoville) 
    while True:
        if len(scoville) == 1:
            if scoville[0] >=K: return count
            else : return -1
        else: 
            first,second = heapq.heappop(scoville), heapq.heappop(scoville)
            if first>=K: return count
            else : heapq.heappush(scoville,first+second*2)
            count +=1    

scoville, K = [1, 2, 3, 9, 10, 12],	7

print(solution(scoville, K))
