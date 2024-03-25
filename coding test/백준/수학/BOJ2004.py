# 팩토리얼로 구하면 시간 초과
# n까지의 k의 배수의 개수 : n / k (k 간격으로 k의 배수가 분포되어 있음)
# n / k, n / k * k, ...
import sys
n, m = map(int, sys.stdin.readline().split())


def count_num(N, k):
    cnt = 0
    while N:
        N = N // k
        cnt += N
    return cnt


five_count = count_num(n, 5) - count_num(m, 5) - count_num(n - m, 5)
two_count = count_num(n, 2) - count_num(m, 2) - count_num(n - m, 2)

if five_count > 0 and two_count > 0:
    print(min(five_count, two_count))
else:
    print(0)
