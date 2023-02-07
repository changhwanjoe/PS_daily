#https://programmers.co.kr/learn/courses/30/lessons/17680?language=python3
from collections import deque

def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize)
    result = 0
    for c in cities :
        c=c.lower()
        if c in cache:
            cache.remove(c)
            cache.append(c)
            result += 1
        else: # cache miss
            cache.append(c)
            result +=5
    answer = result
    return answer