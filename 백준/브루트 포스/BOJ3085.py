import sys
input = sys.stdin.readline

N = int(input())
bf = [list(input().strip()) for _ in range(N)]

max_cnt = 0


def check():
    global max_cnt
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if bf[i][j] == bf[i][j-1]:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1

        cnt = 1
        for j in range(1, N):
            if bf[j][i] == bf[j-1][i]:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1


for i in range(N):
    for j in range(N):
        if j + 1 < N:
            bf[i][j], bf[i][j+1] = bf[i][j+1], bf[i][j]
            check()
            bf[i][j], bf[i][j+1] = bf[i][j+1], bf[i][j]
        if i + 1 < N:
            bf[i][j], bf[i+1][j] = bf[i+1][j], bf[i][j]
            check()
            bf[i][j], bf[i+1][j] = bf[i+1][j], bf[i][j]

print(max_cnt)
