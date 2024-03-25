import sys
input = sys.stdin.readline

k = int(input())
A = list(input().split())
visited = [False] * 10

max_ans = ""
min_ans = ""


def check(i, j, sign):
    if sign == '<':
        return i < j
    else:
        return i > j


def dfs(depth, s):
    global max_ans, min_ans

    if depth == k+1:
        if len(min_ans) == 0:
            min_ans = s
        else:
            max_ans = s
        return

    for i in range(10):
        if not visited[i]:
            if depth == 0 or check(s[-1], str(i), A[depth - 1]):
                visited[i] = True
                dfs(depth + 1, s + str(i))
                visited[i] = False


dfs(0, "")
print(max_ans)
print(min_ans)
