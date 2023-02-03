import sys
N = int(sys.stdin.readline())

print(2**N-1)


def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return
    else:
        hanoi(n - 1, start, 6-start-end)
        print(start, end)
        hanoi(n - 1, 6-start-end, end)


hanoi(N, 1, 3)
