import sys
input = sys.stdin.readline
##############################
from collections import deque

def bfs(x, y):
    v = [[0] * N for _ in range(N)]
    q = deque()
    tlst = []
    
    q.append((x,y))
    v[x][y] = 1
    eat = 0 #distance
    
    while q:
        sx, sy = q.popleft()
        if eat == v[sx][sy]:
            return tlst, eat-1
        
        for i in range(4):
            nx = sx + dx[i]
            ny = sy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and v[nx][ny] == 0 and shark >= space[nx][ny]:
                q.append((nx, ny))
                v[nx][ny] = v[sx][sy] + 1
                if shark > space[nx][ny] > 0: #0은 제외시켜야 함.
                    tlst.append((nx, ny))
                    eat = v[nx][ny]

    return tlst, eat-1

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

shark = 2
cnt = 0
res = 0

for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            x, y = i, j
            space[i][j] = 0
 
while True:
    tlst, dist = bfs(x, y)
    if len(tlst) == 0:
        break
    tlst.sort(key = lambda x: (x[0], x[1]))
    x, y = tlst[0]
    space[x][y] = 0
    cnt += 1
    res += dist
    if cnt == shark:
        shark += 1
        cnt = 0

print(res)
