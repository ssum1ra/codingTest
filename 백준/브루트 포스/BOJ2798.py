import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

n = 0
for i in combinations(card, 3):
    if n < sum(i) and sum(i) <= M:
        n = sum(i)
print(n)
