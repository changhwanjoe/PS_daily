def run_hanoi(n,a,b,c):
    if n == 1: 
        print(a,c)
    else:
        run_hanoi(n-1,a,c,b)
        print(a,c)
        run_hanoi(n-1,b,a,c)
    return 

if __name__ == "__main__":
    n = int(input())

    run_hanoi(n,1,2,3)
