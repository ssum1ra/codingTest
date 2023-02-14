import sys
N = int(sys.stdin.readline())

s = [0] * (N + 1)


s[1] = 9
if N == 2:
    s[2] = 17

for i in range(3, N + 1):
    s[i] = 2 * s[i - 1] - 2

print(s[i] % 1000000000)
