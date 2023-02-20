import sys
input = sys.stdin.readline

N = int(input())

cnt = 0
length_N = len(str(N))

for i in range(length_N - 1):
    cnt += 9 * 10 ** i * (i + 1)

cnt += length_N * (N - 10**(length_N - 1) + 1)

print(cnt)
