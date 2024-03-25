import sys, copy
from itertools import combinations
input = sys.stdin.readline

def solve():
    global res
    for wall_combi in combinations(empty, wall_num):
        tmp_board = copy.deepcopy(board)
        for x, y in wall_combi:
            tmp_board[x][y] = 1
        virus = [(n, m) for n in range(N) for m in range(M) if board[n][m] == 2]
        while virus:
            x, y = virus.pop()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if tmp_board[nx][ny] == 0:
                        tmp_board[nx][ny] = 2
                        virus.append((nx, ny))
        cnt = 0
        for row in tmp_board:
            cnt += row.count(0)
        res = max(res, cnt)


N, M = map(int, input().split())
wall_num = 3
board = [list(map(int, input().split())) for _ in range(N)]
empty = [(n, m) for n in range(N) for m in range(M) if board[n][m] == 0]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

res = 0
solve()
print(res)




