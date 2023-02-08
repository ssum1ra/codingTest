import sys
N = int(sys.stdin.readline())


def lcd(a, b):
    A = a
    B = b
    while B > 0:
        A, B = B, A % B
    return a * b // A


for _ in range(N):
    li = list(map(int, sys.stdin.readline().split()))
    print(lcd(li[0], li[1]))
