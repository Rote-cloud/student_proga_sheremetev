import numpy as np
max_int32 = 2 ** 32 - 1
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
arr = np.where(arr == 0, max_int32, arr)
size = arr.shape[0]

for k in range(size):
       for i in range(size):
              for j in range(size):
                     if i != j and i != k and k != j:
                            arr[i, j] = min(arr[i, j], arr[i, k] + arr[j, k])
print(arr)
n, m = map(int, input().split())
print(arr[n, m])