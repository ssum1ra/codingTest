import sys

N = int(sys.stdin.readline())
li = []
for _ in range(N):
    li.append(list(map(int, sys.stdin.readline().split())))

li.sort(key=lambda x: (x[0], x[1]))

for i in li:
    print(i[0], i[1])
