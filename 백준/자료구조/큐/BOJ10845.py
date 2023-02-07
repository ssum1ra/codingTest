import sys

N = int(sys.stdin.readline())
li = []
for _ in range(N):
    li.append(list(sys.stdin.readline().split()))

num = []
for i in range(N):
    if li[i][0] == "push":
        num.append(int(li[i][1]))
    elif li[i][0] == "pop":
        if num:
            print(num.pop(0))
        else:
            print(-1)
    elif li[i][0] == "size":
        print(len(num))
    elif li[i][0] == "empty":
        if not num:
            print(1)
        else:
            print(0)
    elif li[i][0] == "front":
        if num:
            print(num[0])
        else:
            print(-1)
    elif li[i][0] == "back":
        if num:
            print(num[-1])
        else:
            print(-1)
