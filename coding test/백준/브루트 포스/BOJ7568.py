import sys

N = int(sys.stdin.readline())
li = []
for _ in range(N):
    li.append(list(map(int, sys.stdin.readline().split())))

k = [1] * N
for i in range(N):
    for j in range(i+1, N):
        if li[i][0] > li[j][0] and li[i][1] > li[j][1]:
            k[j] += 1
        elif li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            k[i] += 1

for i in k:
    print(i, end=" ")
