import sys
N = int(sys.stdin.readline())


def star(n):
    if n == 3:
        return ["***", "* *", "***"]
    else:
        temp = []
        origin = star(n / 3)
        for i in range(int(n / 3)):
            temp.append(origin[i] * 3)
        for i in range(int(n / 3)):
            temp.append(origin[i] + " " * int(n / 3) + origin[i])
        for i in range(int(n / 3)):
            temp.append(origin[i] * 3)
        return temp


for i in star(N):
    print(i)
