import sys
n = int(sys.stdin.readline())

li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))

cnt = 0
stack = []
res = []
for i in range(1, n+1):
    stack.append(i)
    res.append('+')
    while stack and stack[-1] == li[cnt]:
        stack.pop()
        res.append('-')
        cnt += 1

if stack:
    print("NO")
else:
    for i in res:
        print(i)

# n 이후부터는 수열이 감소해야 함 (수가 커지는 식으로 스택에 저장되었기 때문)
