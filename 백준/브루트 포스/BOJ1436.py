import sys
N = int(sys.stdin.readline())

num = 0
res = 0
cnt = 0
while cnt != N:
    num += 1
    if "666" in str(num):
        cnt += 1
        res = num
print(res)
