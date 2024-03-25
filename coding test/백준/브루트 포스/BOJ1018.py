import sys

N, M = map(int, sys.stdin.readline().split())

b1 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
      ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']] * 4
b2 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
      ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']] * 4

board = []

for _ in range(N):
    board.append(list(sys.stdin.readline().strip()))

cnt = []
temp = []
for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        cnt1 = 0
        cnt2 = 0
        temp = board[0 + i: 8 + i]
        for k in range(8):
            temp[k] = temp[k][0 + j: 8 + j]

        for k in range(8):
            for a, b in zip(b1[k], temp[k]):
                if a != b:
                    cnt1 += 1
        for k in range(8):
            for a, b in zip(b2[k], temp[k]):
                if a != b:
                    cnt2 += 1

        if cnt1 < cnt2:
            cnt.append(cnt1)
        else:
            cnt.append(cnt2)

print(min(cnt))
