import sys
input = sys.stdin.readline

N, M = map(int, input().split())

s = []
visited = [False] * (N + 1)


def dfs(start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(start, N + 1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs(i + 1)
        s.pop()
        visited[i] = False


dfs(1)
