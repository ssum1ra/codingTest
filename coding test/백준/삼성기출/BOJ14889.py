import sys
input = sys.stdin.readline

def backtracking(depth, ):
    global res
    if  == N // 2:
        start, link = 0, 0
        for i in range(N):
            for j in range(M):
                if visited[i]=True and visited[j]=True:
                    start += S[i][j] 
                elif visited[i]=False and visited[j]=False:
                    link += S[i][j]
        res = min(res, abs(start-link))
    
    for i in range(, N):
        if not visited[i]:
            visited[i] = True
            backtracking()
            visited[i] = False
                            
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
res = sys.maxsize
backtracking(0, 0)
print(res)

