arr = [
    [0, 95, 0, 0, 75, 32, 57, 0],
    [0, 0, 6, 0, 18, 0, 0, 0],
    [0, 0, 0, 7, 0, 0, 11, 0],
    [0, 0, 0, 0, 0, 0, 0, 81],
    [0, 0, 9, 0, 0, 0, 24, 0],
    [0, 5, 0, 0, 0, 0, 20, 16],
    [0, 0, 0, 20, 0, 0, 0, 94],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

source = 0
exit = 7
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
print(way)