#https://www.acmicpc.net/problem/14425
N, M = list(map(int,input().split()))
S = set([input() for _ in range(N)])
strings = [input() for _ in range(M)]
print([True for i in strings if i in S].count(True))