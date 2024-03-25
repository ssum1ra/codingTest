import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

graph = [[0] * (N + 1) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(K):
    x, y = map(int, input().split())
    graph[x][y] = 2

L = int(input())
moves = []
for _ in range(L):
    moves.append(list(map(int, input().split())))

