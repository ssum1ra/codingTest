import sys

N = int(sys.stdin.readline())
num = []
for _ in range(N):
    num.append(int(sys.stdin.readline()))
num.sort()

print(round(sum(num)/N))  # 산술평균
print(num[N//2])  # 중앙값

mode = Counter(num).most_common()
if len(mode) > 1 and mode[0][1] == mode[1][1]:
    print(mode[1][0])
else:
    print(mode[0][0])

print(max(num) - min(num))  # 범위

# dic = {}

# for i in range(len(num)):
#     if num[i] not in dic.keys():
#         dic[num[i]] = 1
#     else:
#         dic[num[i]] += 1

# arr = []
# arr = sorted(dic.items(), key=lambda x: x[1], reverse=True)

# if len(arr) == 1 or arr[0][1] != arr[1][1]:
#     print(arr[0][0])
# else:
#     print(arr[1][0])
