import sys
input = sys.stdin.readline


def dfs(start, depth):
    if depth == 6:
        print(*res)
        return
    for i in range(start, len(s)):
        res.append(s[i])
        dfs(i + 1, depth + 1)
        res.pop()


while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    res = []
    dfs(1, 0)
    print()
