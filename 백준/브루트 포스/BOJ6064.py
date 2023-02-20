# (x-y) % N ==0 으로 푸는 방법은 x를 res라고 생각하면 된다.
# x가 M보다 작을 때 정답이 도출된다면 (M>N) x는 꼭 M으로 나뉘지 않아도 된다.
# x의 초기값이 그대로 정답이 된다.

import sys
input = sys.stdin.readline

cnt = int(input())

for _ in range(cnt):
    M, N, X, Y = map(int, input().split())
    res = X
    while res <= M * N:
        if (res - X) % M == 0 and (res - Y) % N == 0:  # res = pM + x, qN + y
            break
        res += M
    else:
        res = -1
    print(res)
"""
시간 초과
for _ in range(cnt):
    M, N, X, Y = map(int, input().split())
    x = 0
    y = 0
    cnt = 0
    while x != X or y != Y:
        x += 1
        y += 1
        cnt += 1
        if x > M:
            x = 1
        if y > N:
            y = 1
        if x == 1 and y == 1 and cnt > 1:
            cnt = -1
            break
    print(cnt)"""
