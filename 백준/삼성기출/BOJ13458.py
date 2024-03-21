import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

res = 0

for i in range(N):
    A[i] -= B
    res += 1
    if A[i] > 0:
        if A[i] % C == 0:
            res += (A[i] // C)
        else:
            res += (A[i] // C + 1)
            
print(res)