# 스택
import sys
N = int(sys.stdin.readline())

li = []
for _ in range(N):
    li.append(list(sys.stdin.readline().split()))

for i in range(len(li)):
    for j in range(len(li[i])):
        tem = []
        word = list(li[i][j])
        for _ in range(len(word)):
            tem.append(word.pop())
        li[i][j] = "".join(map(str, tem))

for i in li:
    for j in i:
        print(j, end=" ")
    print()

""" 리스트 슬라이스를 통해 구현할 수 있음
array[start:end:step]
array[::-1] """
