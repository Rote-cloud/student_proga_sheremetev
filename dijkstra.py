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
n = int(input())
array, array_s, m, koor_min, num_min = [n], {}, arr.shape[0], n, 0
array_col = [i for i in range(arr.shape[0]) if i != n]
print(array_col)
while len(array) < arr.shape[0]:
       index_min_el = np.argmin(arr[koor_min, :])
       print(arr[koor_min, array_col])
       print(array_col, array)
       if len(array) > 1:
              for j in array_col:
                     arr[koor_min, j] = min(array_s.get(koor_min) + arr[koor_min, j], arr[n, j])
              print(arr[koor_min, :])
       #print(index_min_el)
       #print(arr[index_min_el, :])]
       print(index_min_el)
       num_min = arr[koor_min, index_min_el]
       array_s[index_min_el] = arr[koor_min, index_min_el]
       arr[koor_min, index_min_el], arr[index_min_el, koor_min] = max_int32, max_int32
       if index_min_el not in array:
              array.append(index_min_el)
              array_col.remove(index_min_el)

       koor_min = index_min_el
       n = koor_min
print(dict(sorted(array_s.items())))
print(array_s[int(input())])