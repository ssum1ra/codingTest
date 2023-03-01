import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n

res = 20000


def dfs(idx, depth):
    global res
    if depth == n // 2:
        s1 = 0
        s2 = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    s1 += s[i][j]
                elif not visited[i] and not visited[j]:
                    s2 += s[i][j]
        res = min(res, abs(s1 - s2))
        return
    for i in range(idx, n):
        visited[i] = True
        dfs(i + 1, depth + 1)
        visited[i] = False


dfs(0, 0)
print(res)
