import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

s = []


def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(N):
        s.append(num[i])
        dfs()
        s.pop()


dfs()
