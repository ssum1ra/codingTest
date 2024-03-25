import sys
N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))

m = [10001] * (N + 1)
for i in range(1, N + 1):
    m[i] = P[i - 1]

for i in range(1, N + 1):
    for j in range(1, i//2 + 1):
        m[i] = min(m[i], m[j] + m[i-j])

print(m[N])
