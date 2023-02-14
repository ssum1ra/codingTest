import sys
T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    c = [0] * (n + 1)
    c[1] = 1
    if n > 1:
        c[2] = 2
    if n > 2:
        c[3] = 4
    for i in range(4, n + 1):
        c[i] = c[i - 1] + c[i - 2] + c[i - 3]
    print(c[n])
