print("Введите количество вершин")
m = int(input())
N, array = [], []
for i in range(m):
    arr = list(map(int, input().split(" ")))
    N.append(arr)
for i in range(m):
    for j in range(m - i):
        if N[i][m - j - 1] > 0:
            array.append(N[i][m - j - 1])
array = sorted(array)
arr = [i for i in range(m)]
weight = 0
while(len(set(arr)) > 1):
    min = array[0]
    for i in range(m):
        try:
            index = N[i][:].index(min)
            if arr[i] != arr[index]:
                weight += N[i][index]
                a, b = arr[index], arr[i]
                for j in range(m):
                    if arr[j] == b:
                        arr[j] = a
            N[i][index] = 0
            N[index][i] = 0
        except ValueError:
            continue
    array.pop(0)
print(weight)

