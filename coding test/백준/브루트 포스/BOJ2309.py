# 100이 되는 경우가 여러 개일 수 있음 (여러 개의 정답 배열)
# 따라서 한 정답 배열을 출력한 후 프로그램을 종료시켜야 함.

import sys

li = [0] * 9
for i in range(9):
    li[i] = int(sys.stdin.readline())
li.sort()
for i in range(8):
    for j in range(i + 1, 9):
        if sum(li) - (li[i] + li[j]) == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                else:
                    print(li[k])
            exit()
