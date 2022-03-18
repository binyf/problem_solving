#https://www.acmicpc.net/problem/1660
def get_series(N):
    seq = 1
    n = 1
    series = [seq]
    while True:
        seq += int((n+1)*(n+2)/2)
        if seq > N:
            break
        series.append(seq)
        n += 1
    return series

N = int(input())
series = get_series(N)
dp = [float('inf')]*(N+1)
for i in range(1, N+1):
    for s in series:
        if s > i:
            break
        if s == i:
            dp[i] = 1
            break
        dp[i] = min(dp[i], dp[i-s]+1)
print(dp[N])