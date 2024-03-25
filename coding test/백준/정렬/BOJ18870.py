# 시간초과 (dictionary 탐색 시간 복잡도 O(1) list 탐색 시간 복잡도 O(N))

import sys

N = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
tem = sorted(set(x))
dic = {tem[i]: i for i in range(len(tem))}

for i in x:
    print(dic[i], end=" ")
