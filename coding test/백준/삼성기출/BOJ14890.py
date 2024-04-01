import sys
input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
res = 0

def check(tmp_list):
    visited = [0] * N
    cnt = 1
    for i in range(N-1):
        print(tmp_list[i])
        if visited[i] == 0:
            if tmp_list[i] - tmp_list[i+1] > 1:
                return False
            elif tmp_list[i] - tmp_list[i+1] == 1:
                for j in range(i+1, N-1):
                    if tmp_list[j] != tmp_list[j+1]:
                        break
                    cnt += 1
                if cnt >= L:
                    for j in range(i+1, (i+1)+cnt):
                        if visited[j] == 0:
                            visited[j] = 1
                        else:
                            return False
                    cnt = 1
                else: 
                    return False
            elif tmp_list[i] - tmp_list[i+1] == 0:
                cnt += 1
            elif tmp_list[i] - tmp_list[i+1] == -1:
                if cnt >= L:
                    for j in range((i+1)-cnt, i+1):
                        if visited[j] == 0:
                            visited[j] = 1
                        else:
                            return False
                    cnt = 1
                else:
                    return False
            else:
                return False   
    return True

for i in range(N):
    if check(board[i]):
        res += 1
        print(board[i])

for i in range(N):
    tmp_list = []
    for j in range(N):
        tmp_list.append(board[j][i])
    if check(tmp_list):
        res += 1
        print(tmp_list)
        
print(res)