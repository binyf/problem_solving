#https://www.acmicpc.net/problem/16400
def get_prime(N):
    primes = []
    for i in range(2,N+1):
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes
    
N = int(input())
primes = get_prime(N)
dp = [0] * (N+1)
dp[0] = 1
for p in primes:
    for i in range(p, N+1):
        dp[i] = (dp[i] + dp[i-p]) % 123456789
print(dp[N])