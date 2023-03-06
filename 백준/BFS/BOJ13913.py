from collections import deque
import sys
input = sys.stdin.readline()


def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            return arr[v]
        for nv in (v-1, v+1, v*2):
            if 0 <= nv <= MAX and not arr[nv]:
                arr[nv] = arr[v] + 1
                bfs(nv)


MAX = 10**5 + 1
n, k = map(int, input().split())
arr = [0] * MAX
print(bfs(n))
print()
