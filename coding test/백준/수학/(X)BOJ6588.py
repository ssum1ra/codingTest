# 시간초과

import sys

a = {}
for i in range(1000001):
    a[i] = True

for i in range(2, 1001):
    if a[i]:
        for j in range(i + i, 1000001, i):
            a[j] = False


while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    for i in range(3, (N // 2) + 1):
        if a[i]:
            if a[N-i]:
                sys.stdout.write(str(N) + " = " + str(i) +
                                 " + " + str(N - i) + '\n')
                break
        else:
            if i == N // 2:
                sys.stdout.write("Goldbach's conjecture is wrong.")
                break
