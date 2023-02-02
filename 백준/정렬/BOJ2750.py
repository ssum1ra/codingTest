N = int(input())

num = []

for _ in range(N):
    num.append(int(input()))


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


num = quick_sort(num)

for i in num:
    print(i)

# N = int(input())

# num = []

# for _ in range(N):
#     num.append(int(input()))

# num.sort()

# for i in num:
#     print(i)
