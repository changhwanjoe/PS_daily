def solution(dirs):
    answer = 0
    x,y = 0,0 # 초기좌표 
    trace = [] #    
    dx = [-1, +1, 0, 0 ] #상 하 우 좌
    dy = [0, 0, +1, -1 ]
    
    for direction in dirs :
        if direction == 'U': d = 0
        elif direction == 'D': d = 1
        elif direction == 'R': d = 2
        elif direction == 'L': d = 3
        nx,ny = x+dx[d],y+dy[d]   
        if ((-6 <nx<6) and (-6<ny<6)) : # 넘어가지 않는다면
            if (x,y,nx,ny) not in trace and (nx,ny,x,y) not in trace :
                answer +=1
                trace.append(((x,y,nx,ny)))
            x,y = nx,ny
        
    return answer

