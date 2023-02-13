import sys
import math
n = int(sys.stdin.readline())

count = 0
one = n
two = 0
while one >= 0:
    count += math.factorial(one + two) // (math.factorial(one)
                                           * math.factorial(two))
    n = n - 2
    two += 1
    one -= 2

print(count)
