import sys
input = sys.stdin.readline

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
min_value = 4000000

s = []


def dfs(next, value, visited):
    global min_value

    if len(visited) == n:
        if w[next][0] != 0:
            min_value = min(min_value, value + w[next][0])
        return
    for i in range(n):
        if w[next][i] != 0 and i not in visited and value < min_value:
            visited.append(i)
            dfs(i, value + w[next][i], visited)
            visited.pop()


dfs(0, 0, [0])
print(min_value)
