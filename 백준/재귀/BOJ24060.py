import sys
N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

cnt = 0


def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)


def merge(arr, p, q, r):
    global cnt
    i = p
    j = q + 1
    tem = []
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tem.append(arr[i])
            i += 1
        else:
            tem.append(arr[j])
            j += 1
    while i <= q:
        tem.append(arr[i])
        i += 1
    while j <= r:
        tem.append(arr[j])
        j += 1
    for i in range(len(tem)):
        cnt += 1
        if cnt == K:
            print(tem[i])
        arr[p + i] = tem[i]


merge_sort(A, 0, N - 1)

if cnt < K:
    print(-1)
