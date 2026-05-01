def solution(n, k):
    def converter(n,k):
        if k== 2:
            return bin(n)[2:]
        if k== 8 :
            aa = oct(n)
            return oct(n)[2:]
        if k == 10 : 
            return str(n)

        str_ = ''
        while n > 0:
            n, mod = divmod(n,k)
            str_ += str(mod)
        return str_[::-1] # 역순 

    def is_prime_2(n):
        for i in range(n+1):
            if (i<2):
                return False
            else:
                for j in range(2,i):
                    if(i%j==0):
                        return False
        return True 

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        elif n == 2:
            return True
        else: 
            for i in range(2, n):
                if n % i == 0:
                    return False
        return True
    
    converted = converter(n,k)
    print("cc",converted)
    splitted = converted.split('0')
    answer = 0
    for elem in splitted:
        if not elem :
            continue
        elif elem == '1':
            continue
        elif is_prime_2(int(elem)):
            answer +=1     
    return answer

