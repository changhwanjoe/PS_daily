import collections
from typing import List

def leastInterval( tasks, n):
    counter = collections.Counter(tasks) # Counter({'A': 3, 'B': 3})
    result = 0

    while True:
        sub_count = 0
        # 개수 순 추출
        for task, _ in counter.most_common(n + 1):
            #print(task)
            sub_count += 1
            result += 1
            print("!",counter)
            counter.subtract(task)
            print("@",counter)

            print("d",collections.Counter())
            counter += collections.Counter() # 0 이하인 아이템을 목록에서 완전히 제거
            print("#",counter)


        if not counter:
            break

        result += n - sub_count + 1

    return result

tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
print(leastInterval(tasks, n))