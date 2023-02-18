import sys
input = sys.stdin.readline

n = int(input())
dp = [k for k in range(n+1)]

for i in range(1, n + 1):
    for j in range(1, i):
        if j*j > i:
            break
        if dp[i] > dp[i-j*j]+1:
            dp[i] = dp[i-j*j] + 1
print(dp[n])

"""
시간초과 
dp = [100000] * (N + 1)
dp[1] = 1
for i in range(1, N + 1):
    for j in range(1, i):
        if i**0.5 % 1 == 0:
            dp[i] = 1
        else:
            dp[i] = min(dp[i], dp[j] + dp[i - j])
print(dp[N]) """
