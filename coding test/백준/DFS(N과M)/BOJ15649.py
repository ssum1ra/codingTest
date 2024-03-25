import sys
input = sys.stdin.readline

N, M = map(int, input().split())

s = []
visited = [False] * (N+1)


def dfs():
    if len(s) == M:  # len(s)는 depth를 의미
        print(' '.join(map(str, s)))
        return
    for i in range(1, N + 1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        visited[i] = False


dfs()
