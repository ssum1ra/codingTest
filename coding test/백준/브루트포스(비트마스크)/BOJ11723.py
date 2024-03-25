import sys
input = sys.stdin.readline

M = int(input())
s = set()

for _ in range(M):
    arr = list(input().split())

    if arr[0] == "add":
        s.add(int(arr[1]))
    elif arr[0] == "remove":
        s.discard(int(arr[1]))
    elif arr[0] == "check":
        if int(arr[1]) in s:
            print(1)
        else:
            print(0)
    elif arr[0] == "toggle":
        if int(arr[1]) in s:
            s.discard(int(arr[1]))
        else:
            s.add(int(arr[1]))
    elif arr[0] == "all":
        s = set([i for i in range(1, 21)])
    elif arr[0] == "empty":
        s = set()
