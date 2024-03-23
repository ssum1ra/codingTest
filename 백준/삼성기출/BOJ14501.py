import sys
input = sys.stdin.readline

N = int(input())
t = []
p = []
for _ in range(N):
    v1, v2 = map(int, input().split())
    t.append(v1)
    p.append(v2)
dp = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    if t[i] + i > N:
        dp[i] = dp[i+1]
    else:
        # i일에 상담을 하는 것과 상담을 안 하는 것 중 큰 것을 선택
        dp[i] = max(dp[i+1], dp[t[i] + i] + p[i])
    print(dp)
        
print(dp[0])
