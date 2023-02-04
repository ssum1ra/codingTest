import sys
N = int(sys.stdin.readline())

if N == 1:
    print(0)

for i in range(1, N):
    num = list(map(int, str(i)))
    res = i + sum(num)
    if N == res:
        print(i)
        break
    elif i == N - 1:
        print(0)
