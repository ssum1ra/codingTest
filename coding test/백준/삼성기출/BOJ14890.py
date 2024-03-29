import sys
input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
res = 0

def check(tmp_list):
    visited = [0] * N
    cnt = 1
    for i in range(N-1):
        if abs(tmp_list[i] - tmp_list[i+1]) > 1:
            return False
        else:
            if tmp_list[i] == tmp_list[i+1]:
                cnt += 1
            else:
                if cnt >= L:
                    for j in range((i+1)-cnt, i+1):
                        visited[j] = 1
                    cnt = 1
                else:
                    return False
    return True

for i in range(N):
    if check(board[i]):
        res += 1
        print(board[i])
    
tmp_list = []    
for i in range(N):
    for j in range(N):
        tmp_list.append(board[j][i])
    if check(tmp_list):
        res += 1
        print(tmp_list)
        
print(res)