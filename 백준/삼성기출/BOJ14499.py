import sys
input = sys.stdin.readline

def roll(move):
    if move == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
    elif move == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
    elif move == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
    elif move == 4:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]
        

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
moves = list(map(int, input().split()))

dice = [0] * 6
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in moves:
    if 0 <= x + dx[i-1] < M and 0 <= y + dy[i-1] < N:
        x = x + dx[i-1]
        y = y + dy[i-1]
        roll(i)
        if board[x][y] == 0:
            board[x][y] = dice[5]
        else:
            dice[5] = board[x][y]
            board[x][y] = 0
        print(dice[0])