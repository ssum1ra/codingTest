import sys
N = int(sys.stdin.readline())

p = [0] * (N + 1)
p[1] = 1
for i in range(2, N + 1):
    p[i] = p[i - 2] + p[i - 1]

print(p[N])
