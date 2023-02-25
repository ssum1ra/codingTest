# C++ next_permutation
# 배열 뒤부터 두 개씩 인접한 요소를 탐색했을 때 왼쪽에 있는 요소가 계속 크다면
# 왼쪽에 있는 요소가 작기 전까지 내림차순으로 정렬되어있다고 할 수 있음
# 작은 수를 발견한 경우 ( 그 수 + 1 ) 값과 교환해야 함
# 교환 후, 그 뒤부터 정렬하면 다음 수열이 됨.

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

for i in range(N - 1, 0, -1):
    if arr[i - 1] < arr[i]:
        target = i - 1
        break
else:
    print(-1)
    sys.exit()

for i in range(N - 1, 0, -1):
    if arr[target] < arr[i]:
        arr[i], arr[target] = arr[target], arr[i]
        arr = arr[:target + 1] + sorted(arr[target + 1:])
        print(*arr)
        break
