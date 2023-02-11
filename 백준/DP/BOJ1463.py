import sys
N = int(sys.stdin.readline())

a = [[]] * 1000001
a[1] = [1, 0]
a[2] = [1, 1]
a[3] = [1, 1]
for i in range(4, N + 1):
    count = 0
    num = 0
    temp1 = 1000001
    temp2 = 1000001
    temp3 = 1000001
    if i % 3 == 0:
        temp1 = a[i // 3][1]
    elif i % 2 == 0:
        temp2 = a[i // 2][1]
    temp3 = a[i - 1][1]

    count = min(temp1, temp2, temp3)
    if count == temp1:
        a[i] = [i // 3, count + 1]
    if count == temp2:
        a[i] = [i // 2, count + 1]
    if count == temp3:
        a[i] = [i - 1, count + 1]

print(a[N][1])
