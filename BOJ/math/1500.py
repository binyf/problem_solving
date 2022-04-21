#https://www.acmicpc.net/problem/1500
S, K = list(map(int,input().split()))

q, r = S//K, S%K
t = 1

for _ in range(r):
    t *= q + 1
for _ in range(K-r):
    t *= q

print(t)
