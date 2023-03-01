import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n

res = 20000


def check():
    global res
    s1 = 0
    s2 = 0
    for i in range(n):
        for j in range(n):
            if visited[i] and visited[j]:
                s1 += s[i][j]
            elif not visited[i] and not visited[j]:
                s2 += s[i][j]
    res = min(res, abs(s1 - s2))


def dfs(target):
    if target == n:
        check()
        return

    visited[target] = True
    dfs(target + 1)
    visited[target] = False
    dfs(target + 1)


dfs(0)
print(res)
