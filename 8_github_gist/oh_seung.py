import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input()) # length of rows
m = int(input()) # length of columns

table = [input().split() for _ in range(n)]

person_debt = defaultdict(int)
for i in range(len(table)):
    borrower_name = table[i][0]
    lender_name = table[i][1]
    debt_amount = int(table[i][2])
    if person_debt[borrower_name] : # if exists
        person_debt[borrower_name] -= debt_amount
    else :
        person_debt[borrower_name] = -debt_amount

    if person_debt[lender_name]:
        person_debt[lender_name] += debt_amount
    else :
        person_debt[lender_name] = debt_amount

res = sorted(person_debt.items(),key= (lambda x: x[1]),reverse = False)
min_person = []
min_debt = res[0][1]
min_person.append(res[0][0])
for _ in range(len(res)):
    if res[i][1] == min_debt:
        min_person.append(res[i][0])
    else:
        break

if min_debt >= 0:
    print("Nobody has a negative balance")
else:
    print(sorted(min_person))



