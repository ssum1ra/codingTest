import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

visited = [False] * N
s = []


def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    prev = 0
    for i in range(N):
        if prev == num[i] or visited[i]:
            continue
        visited[i] = True
        s.append(num[i])
        prev = num[i]
        dfs()
        s.pop()
        visited[i] = False


dfs()
