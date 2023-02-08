# 유클리드 호제법
# a와 b의 최대 공약수 G는 a % b의 최대공약수 G'와 같음
import sys
a, b = map(int, sys.stdin.readline().split())

A = a
B = b
R = 1
while R > 0:
    R = A % B
    A = B
    B = R
    # A, B = B, A % B 이런 형태로도 표현 가능
print(A)

print(a * b // A)  # a = G * k, b = G * k' 이므로 a * b = (G * k * k') * G


"""
시간초과

import sys
a, b = map(int, sys.stdin.readline().split())

for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break

for i in range(max(a, b), (a * b) + 1):
    if i % a == 0 and i % b == 0:
        print(i)
        break
"""
