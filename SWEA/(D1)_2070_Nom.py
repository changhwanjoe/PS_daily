T = int(input())
  
for i in range(T):
    data = input()
    d = data.split()
    str = ""
    if int(d[0]) == int(d[1]):
        str = "="
    elif int(d[0]) < int(d[1]):
        str = "<"
    else:
        str = ">"
    print("#%d %s" %(i+1, str))
