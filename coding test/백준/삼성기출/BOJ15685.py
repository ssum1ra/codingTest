import sys
input = sys.stdin.readline

N = int(input)
dragon_curves = [list(map(int, input().split())) for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]