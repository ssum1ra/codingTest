import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rel = [[] for _ in range(n)]
visited = [False] * (2001)

for i in range(m):
    a, b = map(int, input().split())
    rel[a].append(b)
    rel[b].append(a)

res = 0


def dfs(idx, depth):
    global res
    if depth == 4:
        res = 1
        return
    for i in rel[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i, depth + 1)
            visited[i] = False


for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False
    if res:
        break

print(res)
