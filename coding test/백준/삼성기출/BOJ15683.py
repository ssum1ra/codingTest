import sys
input = sys.stdin.readline

N, M = map(int, input().split())
space = [[6]*(M+2)] + [[6]+list(map(int, input().split()))+[6] for _ in range(N)] + [[6]*(M+2)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
cctv = [[], [1], [1,3], [0,1], [0,1,3], [0,1,2,3]]            

def cal(tlst):
    visited = [[0] * (M+2) for _ in range(N+2)]
    
    for i in range(len(lst)):
        si, sj = lst[i]
        rot = tlst[i]
        cctv_type = space[si][sj]
        
        for dr in cctv[cctv_type]: # cctv의 한 방향
            ci, cj = si, sj
            dr = (dr + rot) % 4
            while True:
                ci, cj = ci + dy[dr], cj + dx[dr] 
                if space[ci][cj] == 6:
                    break
                visited[ci][cj] = 1
            
    cnt = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if space[i][j] == 0 and visited[i][j] == 0:
                cnt += 1
    return cnt
           
def dfs(n, tlst):
    global res
    if n == len(lst):
        res = min(res, cal(tlst))
        return
    
    dfs(n+1, tlst+[0])
    dfs(n+1, tlst+[1])
    dfs(n+1, tlst+[2])
    dfs(n+1, tlst+[3])

lst = []
for i in range(1, N+1):
    for j in range(1, M+1):
        if 1 <= space[i][j] <= 5:
            lst.append((i, j))

res = N*M
dfs(0, [])
print(res)