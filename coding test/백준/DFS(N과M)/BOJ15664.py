import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

visited = [False] * N
s = []


def dfs(start):
    if len(s) == M:
        print(*s)
        return
    prev = 0
    for i in range(start, N):
        if visited[i] or prev == num[i]:
            continue
        visited[i] = True
        s.append(num[i])
        prev = num[i]
        dfs(i + 1)
        s.pop()
        visited[i] = False


dfs(0)
