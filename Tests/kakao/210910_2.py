from collections import defaultdict
import datetime
import math 

def solution(fees, records):
    min_time , min_fee, default_min, won= fees
    inout_list = defaultdict(list)
    result = []    
    for elem in records:
        temp = elem.split()
        io_time = temp[0]
        car_num, io_content = temp[1], temp[2]
        inout_list[car_num].append([io_time, io_content])

    for i in inout_list.keys():
        remain = False
        if len(inout_list[i])%2 !=0: # 마지막 출차 없을시
            remain = True
        j = len(inout_list[i])//2
        
        parking_time = 0
        for _ in range(j):
            in_car = inout_list[i].pop(0)
            out_car = inout_list[i].pop(0)

            in_time  = datetime.datetime.strptime(in_car[0],'%H:%M')
            out_time = datetime.datetime.strptime(out_car[0],'%H:%M')
            parking_time += math.ceil((out_time-in_time).seconds/60) # parking time in minutes
        if remain == True:
            in_car = inout_list[i].pop(0)

            in_time  = datetime.datetime.strptime(in_car[0],'%H:%M')
            out_time = datetime.datetime.strptime('23:59','%H:%M')
            parking_time += (out_time-in_time).seconds/60 # parking time in minutes
        if parking_time <= min_time:
            tuition = (min_fee)
        else:
            tuition = min_fee + (math.ceil((parking_time-min_time)/default_min)*won)
            print(tuition)
        result.append([i, tuition])
    answer = []
        
    for _ in sorted(result):
        answer.append(_[1])
    return answer

fees = [180, 5000, 10, 600]
records= ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
result  = [14600, 34400, 5000]
print(solution(fees,records))
