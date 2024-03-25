import sys

N = int(sys.stdin.readline())
li = []
for _ in range(N):
    li.append(sys.stdin.readline().strip())

li = list(set(li))

li.sort(key=lambda x: (len(x), x))

for i in li:
    print(i)
