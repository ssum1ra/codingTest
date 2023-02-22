import sys
input = sys.stdin.readline

N, M = map(int, input().split())

s = []


def dfs():
    if len(s) == M:
        print(' '.join(list(map(str, s))))
        return
    for i in range(1, N + 1):
        s.append(i)
        dfs()
        s.pop()


dfs()
