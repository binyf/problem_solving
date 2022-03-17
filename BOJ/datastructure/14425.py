#https://www.acmicpc.net/problem/14425
N, M = list(map(int,input().split()))
S = [input() for _ in range(N)]
strings = [input() for _ in range(M)]
print([i == j for i in S for j in strings].count(True))