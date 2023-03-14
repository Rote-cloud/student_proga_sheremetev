import math
koor = list(map(float, input().split(" ")))
s = list(map(float, input().split(" ")))
f = list(map(float, input().split(" ")))
answer = 0
def koordin(koor1, koor2):
    return math.sqrt(koor1 * koor1 + koor2 * koor2)

for i in range(len(s)):
    koor_rez = abs(s[(i + 2) % 3] - f[(i + 2) % 3])
    if koor[i] == max(s[i], f[i]) and min(s[i], f[i]) == 0:
        answer += round(min(koordin(s[(i + 1) % 3] + koor[i] + f[(i + 1) % 3], koor_rez), koordin(2 * koor[(i + 1) % 3] - f[(i + 1) % 3] - s[(i + 1) % 3] + koor[i], koor_rez), koordin(2 * koor[(i + 2) % 3] - f[(i + 2) % 3] - s[(i + 2) % 3] + koor[i], koor_rez), koordin(f[(i + 2) % 3] + s[(i + 2) % 3] + koor[i], koor_rez)), 3)
        break
    elif ((koor[i] == s[i] and koor[i] == f[i]) or (s[i] == 0 and f[i] == 0)):
        answer += round(koordin(s[(i + 1) % 3] - f[(i + 1) % 3], koor_rez), 3)
        break
    elif ((s[i] not in [0, koor[i]] and f[i] not in [0, koor[i]]) or ((s[i] - f[i]) == 0)) and (s[(i + 1) % 3] not in [0, koor[(i + 1) % 3]] or f[(i + 1) % 3] not in [0, koor[(i + 1) % 3]]):
            answer += round(koordin(koor_rez + abs(s[(i + 1) % 3] - f[(i + 1) % 3]), abs(s[i] - f[i])), 3)
            break
print(answer)

