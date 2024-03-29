import sys
input = sys.stdin.readline

def dfs(depth, ):
    global min_num
    global max_num
    if depth == N:
        return
    
    

N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))

min_num = sys.maxsize
max_num = 0
    