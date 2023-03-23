import numpy as np
max_int32 = float('inf')
arr = np.array([[0, 7, 0, 0, 9, 2, 0, 0, 0, 0, 0, 0],
       [7, 0, 5, 4, 8, 2, 0, 0, 0, 0, 0, 0],
       [0, 5, 0, 2, 9, 0, 0, 0, 0, 0, 0, 0],
       [0, 4, 2, 0, 3, 0, 8, 3, 0, 0, 0, 0],
       [9, 8, 9, 3, 0, 3, 5, 1, 7, 0, 0, 0],
       [2, 2, 0, 0, 3, 0, 0, 6, 1, 0, 0, 0],
       [0, 0, 0, 8, 5, 0, 0, 6, 0, 4, 4, 0],
       [0, 0, 0, 3, 1, 6, 6, 0, 2, 7, 8, 5],
       [0, 0, 0, 0, 7, 1, 0, 2, 0, 0, 6, 1],
       [0, 0, 0, 0, 0, 0, 4, 7, 0, 0, 10, 0],
       [0, 0, 0, 0, 0, 0, 4, 8, 6, 10, 0, 3],
       [0, 0, 0, 0, 0, 0, 0, 5, 1, 0, 3, 0]])
N = arr.shape[0]
arr_way = np.zeros((N, N))
arr_way = np.where(arr_way == 0, max_int32, arr_way)
arr = np.where(arr == 0, max_int32, arr)
n = int(input())
arr_way[0][n] = 0
for i in range(N - 1):
       for j in range(N):
              arr_way[i + 1][j] = arr_way[i][j]
              for k in range(N):
                     arr_way[i + 1][j] = min(arr_way[i + 1][j], arr_way[i][k] + arr[k][j])

print(arr_way.astype(int))