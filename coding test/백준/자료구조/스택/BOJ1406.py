""" 시간초과
append(): O(1)
pop(): O(1)
insert(): O(N) """

import sys
stack1 = list(sys.stdin.readline().strip())
M = int(sys.stdin.readline())
li = []
for _ in range(M):
    li.append(list(sys.stdin.readline().split()))

stack2 = []
for i in range(M):
    if li[i][0] == "L":
        if stack1:
            stack2.append(stack1.pop())
    elif li[i][0] == "D":
        if stack2:
            stack1.append(stack2.pop())
    elif li[i][0] == "B":
        if stack1:
            stack1.pop()
    elif li[i][0] == "P":
        stack1.append(li[i][1])


for i in stack1:
    print(i, end='')
for i in reversed(stack2):
    print(i, end='')
