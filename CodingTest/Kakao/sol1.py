def solution(new_id):
    # case1:
    id = new_id.lower()

    # case2:
    j=0
    for i in id:
        j+=1
        if i.isalnum():
            pass
        elif i == '-' or i=='_' or i=='.':
            pass
        else:
            id = id.replace(i,'')

    # case3:
    while '..' in id:
        id = id.replace('..', '.')

    # case4:
    if id.startswith('.'):
        id = id[1:]
    elif id.endswith('.'):
        id = id[:-1]

    # case5:
    if id == '' :
        id = 'a'

    # case6:
    if len(id) >= 16:
        id = id[:15]

    if id.endswith('.'):
        id = id[:-1]

    # case7:
    if len(id) <= 2:
        while (len(id) < 3):
            id += id[-1]

    return(id)