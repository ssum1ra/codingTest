import sys
N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in li:
    if i == 2:
        cnt += 1

    for j in range(2, i):
        if i % j == 0:
            break
        else:
            if j == i-1:
                cnt += 1

print(cnt)
