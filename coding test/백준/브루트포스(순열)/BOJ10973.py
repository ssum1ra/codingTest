import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

for i in range(n - 1, 0, -1):
    if arr[i - 1] > arr[i]:
        target = i - 1
        break
else:
    print(-1)
    sys.exit()

for i in range(n - 1, 0, -1):
    if arr[target] > arr[i]:
        arr[target], arr[i] = arr[i], arr[target]
        arr = arr[:target + 1] + sorted(arr[target + 1:], reverse=True)
        print(*arr)
        break
