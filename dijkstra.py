import numpy as np

def dijkstra(arr, start):
       max_int = float('inf')
       n = start
       array, m, koor_min, num_min = [n], arr.shape[0], n, 0
       array_s = {i: float('inf') for i in range(m)}
       array_col = [i for i in range(arr.shape[0]) if i != n]
       while len(array) < m:
              if len(array) > 1:
                     for j in array_col:
                            arr[koor_min, j] = min(array_s.get(koor_min) + arr[koor_min, j], arr[n, j])
              index_min_el = np.argmin(arr[koor_min, :])
              if array_s[index_min_el] == max_int:
                     array_s[index_min_el] = arr[koor_min, index_min_el]
              arr[koor_min, index_min_el], arr[index_min_el, koor_min] = max_int, max_int
              if index_min_el not in array:
                     array.append(index_min_el)
                     array_col.remove(index_min_el)
              n = koor_min
              koor_min = index_min_el
       del array_s[start]
       return array_s

