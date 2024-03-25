N, k = input().split()
x = list(reversed(sorted(map(int, input().split()))))
print(x[int(k) - 1])
