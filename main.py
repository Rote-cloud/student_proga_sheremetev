n = int(input())
arr = sorted(map(int, input().split(" ")))
arr_end = []
arr_test = []
count = arr.count(1)
count_max = 0
if count > 0:
    del arr[0:count]
l = len(arr)
i = 0
while len(arr) > 1:
    count_max = 1
    arr_test = []
    arr_test.append(arr[i])
    num = arr[i] ** 2
    arr.pop(i)
    if num > max(arr):
        break
    try:
        a = arr.index(num)
        count_max += 1
        arr_test.append(arr[a])
        arr.pop(a)
        while a < max(arr):
            if count_max > count:
                count = count_max
                arr_end = arr_test
            a = arr.index(arr[a] ** 2)
            count_max += 1
            arr_test.append(arr[a])
            arr.pop(a)
        print(arr_end)
    except Exception:
        continue
print(arr)
print(count)
print(arr_end)