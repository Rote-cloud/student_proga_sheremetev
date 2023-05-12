def dfs(arr, source):
    n = len(arr)
    visited = [False] * n
    stack = [source]
    out = [source]
    visited[source] = True

    while stack:
        vertex = stack.pop(0)
        for i in range(n):
            if not visited[i] and arr[vertex][i] > 0:
                visited[i] = True
                stack.append(i)
                out.append(i)

    return out

arr = [[1, 1, 1, 0, 0],
       [1, 1, 1, 0, 0],
       [1, 1, 1, 0, 0],
       [0, 0, 0, 1, 1],
       [0, 0, 0, 1, 1]]
count = 0
arr_out = []
for i in range(len(arr)):
    out = sorted(dfs(arr, i))
    if out not in arr_out:
        count += 1
        arr_out.append(out)
print(count)
print(arr_out)