# 범위를 100만으로 지정한 이유
# 이동하고 싶은 채널의 범위 : 0 ~ 500,000
# 이 때, 누를 수 있는 버튼이 9뿐이라면 999,999로 부터 빼야하는 경우도 고려해야 하므로

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
numbers = list(map(int, input().split()))

min_cnt = abs(100 - N)
for i in range(1000001):
    for j in str(i):
        if int(j) in numbers:
            break
    else:
        min_cnt = min(abs(N - i) + len(str(i)), min_cnt)

print(min_cnt)
