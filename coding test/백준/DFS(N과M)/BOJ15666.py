import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

s = []


def dfs(start):
    if len(s) == M:
        print(*s)
        return
    temp = 0
    for i in range(start, N):
        if temp == numbers[i]:
            continue
        s.append(numbers[i])
        temp = numbers[i]
        dfs(i)
        s.pop()


dfs(0)
