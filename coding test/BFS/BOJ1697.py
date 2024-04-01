import sys
from collections import deque


def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            return arr[v]
        for nv in (v-1, v+1, 2*v):
            if 0 <= nv < MAX and not arr[nv]:
                arr[nv] = arr[v] + 1
                q.append(nv)


MAX = 100001
n, k = map(int, sys.stdin.readline().split())
arr = [0] * MAX
print(bfs(n))
