import numpy as np
N = np.array([
    [0, 4, 0, 3, 6, 1, 0],
    [4, 0, 2, 3, 7, 6, 1],
    [0, 2, 0, 0, 4, 0, 2],
    [3, 3, 0, 0, 1, 5, 3],
    [6, 7, 4, 1, 0, 3, 6],
    [1, 6, 0, 5, 3, 0, 7],
    [0, 1, 2, 3, 6, 7, 0]
])
print("Введите количество вершин")
m = int(input())
N = []
for i in range(m):
    N.append(list(map(int, input().split(" "))))
print("Введите вершину")
n = int(input())
arr = [n]
weight = 0
suma = int((1 + m) / 2 * m)
while(sum(arr) < suma):
    coor, min = 0, np.max(N)
    for i in arr:
        for j in range(m):
            if min >= N[i - 1][j] and N[i - 1][j] > 0 and j + 1 not in arr:
                min, coor = N[i - 1][j], j + 1
    if coor > 0:
        weight += min
        arr.append(coor)
print(weight)


