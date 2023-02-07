
# Problem 2

def solution(a, b, m):
    answer = 0
    return answer

    def dfs(number,M):
        for j in range(0,20):
            for i in range(0,m+1):
                result = dfs(j,i)
                if result :
                    return ans
        if isSameTree(a,b):
            return True
    
    dfs(0,0)
    return M
    number = 0, M =0 ~ m
    number =1, M = 0~ m 
    number =2 , M = 0~ m

class TreeNode():
    def __init__(self, x: int) -> None:
        self.val = x
        self.left = None
        self.right = None

def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:        
        if p==None and q==None :
            return True

        if p==None or q==None :
            return False

        return (p.val==q.val) and (self.isSameTree(p.left,q.left)) and (self.isSameTree(p.right,q.right))

    
class TreeNode():
    def __init__(self, x: int) -> None:
        self.val = x
        self.left = None
        self.right = None
def isSame(a,b):
    for elm in a:
        if elm not in b:
            return False
    return True
    new_a,new_b=[],[]
    for elm_a,elm_b in zip(a,b):
        elm_a.sort()
        elm_b.sort()
        new_a.append(elm_a)
        new_b.append(elm_b)
        new_a.sort()
        new_b.sort()
    if new_a == new_b :
        return True
    else:
        return False

from itertools import combinations
# 2개의 조합으로 만들수 있는 경우의 수 
a=[1,2,3,4,5]
c = list(combinations(a, 2))  # 조합
set_list =[]
for elm in c:
    set_list.append(set(elm))
def solution(a, b, m):
    def rule1(arr): # 연결 하나를 없애고, 연결하나를 추가 [1,2] 없애고, [1,3]추가
        check = []
        for _ in range(len(b)):
            check.append(b.pop(0))
            for elm in set_list:
                if elm not in b and elm not in check:
                    b.append(elm)
                    if isSame(a,b):
                        return True
        return False
    def ruel2(arr): # 두 정점을 바꿈 -> 모든 elment 에 대해 숫자를 교체
        for elm in set_list:
            

    pass
    answer = 0
    new_a,new_b =[],[]
    for elm_a,elm_b in zip(a,b):
        new_a.append(set(elm_a))
        new_b.append(set(elm_b))
    if isSame(new_a,new_b):
        return 0
        
    def dfs(number,M):
        for j in range(0,20):
            for i in range(0,m+1):
                result = dfs(j,i)
                if result :
                    return ans
        if isSame(new_a,new_b):
            return j
        
    return answer

    # def dfs(number,M):
    #     for j in range(0,20):
    #         for i in range(0,m+1):
    #             result,ans = dfs(j,i)
    #             if result :
    #                 return ans
    #     if 
    
    # number = 0, M =0 ~ m
    # number =1, M = 0~ m 
    # number =2 , M = 0~ m


