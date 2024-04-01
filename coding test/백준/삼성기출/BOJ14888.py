import sys
input = sys.stdin.readline

def dfs(depth, value):
    global min_res, max_res
    
    if depth == N - 1:
        min_res = min(min_res, value)
        max_res = max(max_res, value)
        return
    
    if op[0] > 0:
        op[0] -= 1
        dfs(depth + 1, value + A[depth + 1])
        op[0] += 1
        
    if op[1] > 0:
        op[1] -= 1
        dfs(depth + 1, value - A[depth + 1])
        op[1] += 1
        
    if op[2] > 0:
        op[2] -= 1
        dfs(depth + 1, value * A[depth + 1])
        op[2] += 1
        
    if op[3] > 0:
        op[3] -= 1
        dfs(depth + 1, int(value / A[depth + 1]))
        op[3] += 1

N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))

min_res = sys.maxsize
max_res = -sys.maxsize

dfs(0, A[0])

print(max_res)
print(min_res)