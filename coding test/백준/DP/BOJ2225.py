# dp[i-1][j] 맨 뒤 숫자 + 1
# dp[i][j-1] 맨 뒤에 0 추가
# 하게 되면 모든 경우의 수를 알 수 있음
# (왜냐하면 0으로 끝나는 경우와 다른 수로 끝나는 경우가 구분되기 때문)
# 따라서 d[i] = dp[i-1][j] + dp[i][j-1]
import sys
N, K = map(int, sys.stdin.readline().split())

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(N+1):
    for j in range(1, K+1):
        if i == 0 or j == 1:
            dp[i][j] = 1

for i in range(1, N + 1):
    for j in range(2, K+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[N][K] % 1000000000)
