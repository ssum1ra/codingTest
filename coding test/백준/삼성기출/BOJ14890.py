import sys
input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def check(line):
    global L
    visited = [False for _ in range(N)]
    for i in range(N-1):
        if line[i] == line[i+1]:
            continue
        elif abs(line[i]-line[i+1]) > 1:
            return False
        elif line[i] > line[i+1]:
            temp = line[i + 1]
            for j in range(i+1, i+L+1):
                if 0 <= j < N:
                    if temp != line[j]:
                        return False
                    elif visited[j]:
                        return False
                    visited[j] = True
                else:
                    return False
        else:
            temp = line[i]
            for j in range(i, i-L, -1):
                if 0 <= j < N:
                    if temp != line[j]:
                        return False
                    elif visited[j]:
                        return False
                    visited[j] = True
                else:
                    return False
    return True

res = 0

for i in board:
    if check(i):
        res += 1

for i in range(N):
    temp = []
    for j in range(N):
        temp.append(board[j][i])
    if check(temp):
        res += 1
                
print(res)
    