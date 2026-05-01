def filter_list(l):
    li = []
    for c in l:
        if type(c) == int :
            li.append(c)
        
    return li

def filter_list2(l):
    return [i for i in l if type(i) is not str]
    return [i for i in l if not isinstace(i, str)]
  #'return a new list with the strings filtered out'