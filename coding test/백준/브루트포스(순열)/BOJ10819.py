# 배열에 있는 수들이 같을 수도 있음
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
visited = [False] * n
res = 0

s = []


def dfs():
    global res
    if len(s) == n:
        temp = 0
        for i in range(n - 1):
            temp += abs(s[i] - s[i + 1])
        res = max(res, temp)
        return

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        s.append(arr[i])
        dfs()
        s.pop()
        visited[i] = False


dfs()
print(res)
