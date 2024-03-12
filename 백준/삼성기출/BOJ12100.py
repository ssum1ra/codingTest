import sys
input = sys.stdin.readline

N = int(input())
board = [list(input().rstrip()) for _ in range(N)]

def left(board):
    for i in range(N):
        
