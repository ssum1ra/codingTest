import sys
input = sys.stdin.readline

def backtracking(depth, idx):
    global res
    if depth == N // 2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i]==True and visited[j]==True:
                    start += S[i][j] 
                elif visited[i]==False and visited[j]==False:
                    link += S[i][j]
        res = min(res, abs(start-link))
        return
    
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            backtracking(depth+1, i+1)
            visited[i] = False
                            
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
res = sys.maxsize
backtracking(0, 0)
print(res)

