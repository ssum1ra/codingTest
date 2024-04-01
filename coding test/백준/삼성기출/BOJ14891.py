import sys
from collections import deque

input = sys.stdin.readline

def left(idx, d):
    if idx < 0:
        return
    if gears[idx][2] != gears[idx + 1][6]:
        left(idx - 1, -d)
        gears[idx].rotate(d)

def right(idx, d):
    if idx > 3:
        return
    if gears[idx - 1][2] != gears[idx][6]:
        right(idx + 1, -d)
        gears[idx].rotate(d)
        
gears = [deque(list(map(int, input().rstrip()))) for _ in range(4)]
K = int(input())

for _ in range(K):
    idx, d = map(int, input().split())
    idx -= 1
    left(idx - 1, -d)
    right(idx + 1, -d)
    gears[idx].rotate(d)

res = 0
for i in range(4):
    if gears[i][0] == 1:
        res += 2**i
print(res)