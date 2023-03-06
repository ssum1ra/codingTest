import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]

visited1 = [False] * (n + 1)
visited2 = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True


def dfs(idx):
    visited1[idx] = True
    print(idx, end=' ')
    for i in range(1, n + 1):
        if not visited1[i] and graph[idx][i]:
            dfs(i)


def bfs(idx):
    q = deque([idx])
    visited2[idx] = True
    while q:
        idx = q.popleft()
        print(idx, end=" ")
        for i in range(1, n + 1):
            if not visited2[i] and graph[idx][i]:
                q.append(i)
                visited2[i] = True


dfs(v)
print()
bfs(v)
