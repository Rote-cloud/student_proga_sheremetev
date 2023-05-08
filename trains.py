import numpy as np

n = int(input())
max_el = 0
list_arr = []
for i in range(n):
    input_arr = [int(i) for i in input().split(" ")]
    max_el = max(max_el, input_arr[1])
    list_arr.append(input_arr)

arr = np.ones((max_el, max_el))
for el in list_arr:
    arr[el[0] - 1, el[1] - 1] = el[2]
arr = [list(arr[i, :]) for i in range(max_el)]

source = 0
exit = max_el - 1
parent = [-1] * len(arr)
way = 0

def dfs(arr, source, exit, parent):
    n = len(arr)
    visited = [False] * n
    stack = [source]
    visited[source] = True

    while stack:
        vertex = stack.pop(0)
        for i in range(n):
            if not visited[i] and arr[vertex][i] > 0:
                visited[i] = True
                parent[i] = vertex
                stack.append(i)

    return visited[exit]

while True:
    wh_break = dfs(arr, source, exit, parent)
    max_int = float('inf')
    if wh_break == False:
        break
    min_way = exit
    while min_way != source:
        index = parent[min_way]
        max_int = min(max_int, arr[index][min_way])
        min_way = index
    way += max_int

    vertex_subtraction = exit
    while vertex_subtraction != source:
        par = parent[vertex_subtraction]
        arr[par][vertex_subtraction] -= max_int
        arr[vertex_subtraction][par] += max_int
        vertex_subtraction = par
print(way * 24)