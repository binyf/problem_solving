#https://www.acmicpc.net/problem/1907
from itertools import product
equation = input().split('=')
left = equation[0].split('+')
form = [left[0], left[1], equation[1]]
num = []
for M in form:
    cnt = {'C' : 0, 'H' : 0, 'O': 0}
    for i in range(len(M)):
        if M[i].isdigit():
            cnt[M[i-1]] += int(M[i])-1
        else:
            cnt[M[i]] += 1 
    num.append(cnt)
for a, b, c in product(range(1,11), range(1,11), range(1,11)):
    if [num[0][m]*a+num[1][m]*b for m in num[0]] == [num[2][m]*c for m in num[2]]:
        print(a,b,c)
        break
