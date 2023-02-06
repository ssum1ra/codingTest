import sys
N = int(sys.stdin.readline())
p = []
for _ in range(N):
    p.append(list(sys.stdin.readline().strip()))

for i in p:
    temp = []
    for j in i:
        if j == ')':
            if temp:
                temp.pop()
            else:
                temp.append(j)
                break
        elif j == '(':
            temp.append(j)
    if temp:
        print("NO")
    else:
        print("YES")
