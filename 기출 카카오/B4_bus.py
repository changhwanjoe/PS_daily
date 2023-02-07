def solution(n, t, m, timetable):
    timetable = [int(time[:2])*60+int(time[3:]) for time in timetable]
    timetable.sort()
    current = 9*60
    arrival_table = [9*60+i*t for i in range(n)]
    for _ in range(n):
        for _ in range(m):
            if timetable and timetable[0]<=current:
                candidate = timetable.pop(0) -1
            else:
                candidate = current
        current +=t 
    s,r = divmod(candidate,60)
    answer = str(s).zfill(2)+":"+str(r).zfill(2)
    return answer