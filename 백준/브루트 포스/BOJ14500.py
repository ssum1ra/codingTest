import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

res = 0


def dfs(x, y, total, depth):
    global res

    if depth == 3:
        res = max(res, total)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny]:
            continue

        if depth == 1:
            visited[nx][ny] = True
            dfs(x, y, total + board[nx][ny], depth + 1)
            visited[nx][ny] = False

        visited[nx][ny] = True
        dfs(nx, ny, total + board[nx][ny], depth + 1)
        visited[nx][ny] = False


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, board[i][j], 0)
        visited[i][j] = False

print(res)
