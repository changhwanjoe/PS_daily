from collections import deque
import heapq
stack = deque()
heap = []
    # heapq.heappop(heap)
    # heapq.heappush(heap,())
def solution(arr, processes):
    p_li = [p.split() for p in processes]
    new_p_li = deque()
    for elm in p_li:
        temp = []
        if elm[0]=="read":
            temp.append(-1)
        elif elm[0] == "write":
            temp.append(-2)
        temp.extend(list(map(int,elm[1:])))
        new_p_li.append(temp)
    # new_p_li = [[-2, 1, 3, 1, 2], [-2, 2, 6, 4, 7], [-2, 4, 3, 3, 5, 2], [-2, 5, 2, 2, 5], [-2, 6, 1, 3, 3, 9], [-2, 9, 1, 0, 7]]
    
    def read(start:int,end:int)->str :
        temp = ""
        for i in range(start,end+1):
            temp+=str(arr[i])
        return temp
    
    def write(start:int,end:int,number:int) ->None:
        for i in range(start,end+1):
            arr[i]=str(number)

    def do_process(ps):
        ps_type     = ps[0]
        time_start  = ps[1]
        time_durat  = ps[2]
        idx_s       = ps[3]
        idx_e       = ps[4]
        if ps_type == -2: # write
            c_num = ps[5]
            write(idx_s,idx_e,c_num)
        if ps_type == -1: # read
            result.append(read(idx_s,idx_e))

    waiting_heap = []
    processing = [] #'r', left_time or "w"_left_time
    start_time = 0
    end_time = 0
    result = []
    #프로세싱 ['r',time]
    
    while processing or waiting_heap or new_p_li:
        if new_p_li:
            ps = new_p_li.popleft()
            ps_type     = ps[0]
            time_start  = ps[1]
            time_durat  = ps[2]
            idx_s       = ps[3]
            idx_e       = ps[4]
            if ps[0] == -2:
                c_num = ps[5]
        
        if processing:
            if processing[0][1]+processing[0][2] <=end_time: # something in processing, but duration is finished
                processing.pop()

        if waiting_heap ==[] and processing==[]: # nothing     
            processing.append(ps)
            do_process(ps)
            
        elif processing==[] and waiting_heap !=[]: # nothing proceed, but in waiting 
            processing.append(heapq.heappop(waiting_heap)) # put waiting into process

        elif processing[0][0] == -1 and new_p_li : # something in process, and its reading
            if ps_type == -1: # new process is reading 
                if waiting_heap==[]: # nothing in waiting 
                    p_ps = processing.pop()
                    if ps[1]+ps[2] > p_ps[1]+p_ps[2]: #final_time 
                        processing.append(ps)
                    else:
                        processing.append(p_ps)
                    do_process(ps)
                else: # writing is waiting 
                    heapq.heappush(waiting_heap, ps)
            elif ps_type == -2 : # new process is writing a
                heapq.heappush(waiting_heap, ps)
        
        elif processing[0][0] == -2 : # something in process, and its writing 
            heapq.heappush(waiting_heap, ps)

        end_time +=1           
        
    answer = []
    return answer

# 누가 쓰고 있을땐 읽기, 쓰기 모두 대기
# 누가 읽고 있을때, 쓰기는 대기, 읽기는 즉시 가능
# 하나의 쓰기가 대기중이면, 읽기도 대기 

# 대기중인 쓰기를 읽기보다 먼저 수행
# 쓰기끼리는 순서 있음


arr = ["1","2","4","3","3","4","1","5"]
processes = ["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]
res = ["24","3415","4922","12492215","13"]
solution(arr,processes)

# arr =["1","1","1","1","1","1","1"]
# processes =["write 1 12 1 5 8","read 2 3 0 2","read 5 5 1 2","read 7 5 2 5","write 13 4 0 1 3","write 19 3 3 5 5","read 30 4 0 6","read 32 3 1 5"]
# res = ["338","38","8888","3385551","38555","29"]