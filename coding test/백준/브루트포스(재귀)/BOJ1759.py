import sys
input = sys.stdin.readline

L, C = map(int, input().split())
arr = list(input().split())
arr.sort()

s = []


def dfs(start):
    if len(s) == L:
        v, c = 0, 0

        for i in range(L):
            if s[i] in ['a', 'e', 'i', 'o', 'u']:
                v += 1
            else:
                c += 1
        if v >= 1 and c >= 2:
            print("".join(s))
        return

    for i in range(start, C):
        s.append(arr[i])
        dfs(i + 1)
        s.pop()


dfs(0)
