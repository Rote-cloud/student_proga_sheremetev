n, m = map(int, input().split())
xn, yn, zn = map(int, input().split())
def movement(n, x, y):
    return [y, n - x + 1]
for i in range(m):
    a, k, s = map(str, input().split())
    k, s = int(k), int(s)
    if a == "X" and k == xn:
        if s == 1:
            yn, zn = movement(n, yn, zn)
        else:
            zn, yn = movement(n, zn, yn)
    if a == "Y" and k == yn:
        if s == 1:
            xn, zn = movement(n, xn, zn)
        else:
            zn, xn = movement(n, zn, xn)
    if a == "Z" and k == zn:
        if s == 1:
            xn, yn = movement(n, xn, yn)
        else:
            yn, xn = movement(n, yn, xn)
print(xn, yn, zn)