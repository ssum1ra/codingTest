import sys
N = int(sys.stdin.readline())

li = []
for _ in range(N):
    li.append(list(sys.stdin.readline().split()))

num = []
for i in li:
    if i[0] == "push":
        num.append(int(i[1]))
    elif i[0] == "pop":
        if not num:
            print(-1)
        else:
            print(num[len(num)-1])
            del num[len(num)-1]
    elif i[0] == "size":
        print(len(num))
    elif i[0] == "empty":
        if not num:
            print(1)
        else:
            print(0)
    elif i[0] == "top":
        if num:
            print(num[len(num) - 1])
        else:
            print(-1)
