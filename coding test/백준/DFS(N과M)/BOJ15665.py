import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers = sorted(set(numbers))

s = []


def dfs():
    if len(s) == M:
        print(*s)
        return
    for i in numbers:
        s.append(i)
        dfs()
        s.pop()


dfs()
