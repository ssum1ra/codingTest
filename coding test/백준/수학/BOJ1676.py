# 재귀 시 런타임 에러
# Math.factorial을 써도 될 듯

import sys
N = int(sys.stdin.readline())

res = 1
for i in range(1, N + 1):
    res = res * i


cnt = 0
while True:
    if res % 10 == 0:
        res = res // 10
        cnt += 1
    else:
        print(cnt)
        break
