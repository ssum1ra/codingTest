# input()으로 입력받게 되면 많은 시간 소요됨.
# 따라서 시간을 단축하기 위해 sys.stdin.readline()을 이용해야함.

import sys

N = int(input())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

for i in arr:
    sys.stdout.write(str(i) + "\n")
