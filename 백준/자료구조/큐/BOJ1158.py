# 시간 초과
# 순환 큐
# 리스트를 pop(0)할 때 시간초과, 큐를 사용해야 한다면 더 빠른 deque 사용
from collections import deque
import sys
N, K = map(int, sys.stdin.readline().split())

li = deque()
for i in range(1, N + 1):
    li.append(i)

res = []
while li:
    for _ in range(K - 1):
        li.append(li.popleft())
    res.append(li.popleft())


print("<", end='')
print(*res, sep=', ', end='')
print(">", end='')
