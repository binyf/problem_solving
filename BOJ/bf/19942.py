#https://www.acmicpc.net/problem/19942
N = int(input())
mp, mf, ms, mv =  map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

indices = list(range(2**N))
indices = ['0'*(N-len(str(bin(idx)[2:]))) + str(bin(idx)[2:]) for idx in indices]
C = []
for idx in indices:
    cost = 0
    g = []
    p, f, s, v = 0, 0, 0, 0
    for i in range(len(idx)):
        if idx[i] == '1':
            p, f, s, v, cost = p+mat[i][0], f+mat[i][1], s+mat[i][2], v+mat[i][3], cost+mat[i][4]
            g.append(i+1)
    if p >= mp and f >=mf and s >= ms and v >= mv:
        C.append([cost, g])
C.sort()
if C:
    ans = C[0]
    print(ans[0])
    print(*ans[1])
else: 
    print(-1)
