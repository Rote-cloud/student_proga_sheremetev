spells = {"MIX": ["MX", "XM"],
          "WATER": ["WT", "TW"],
          "DUST": ["DT", "TD"],
          "FIRE" : ["FR", "RF"]}

actions = []
n = 0
while n != 100:
    action = input().split(" ")
    if action[0] == "end":
        break
    s = spells[action[0]][0]
    for i in range(1, len(action)):
        if action[i].isdigit():
            s += actions[int(action[i]) - 1]
        else:
            s += action[i]
    s += spells[action[0]][1]
    actions.append(s)
    n += 1
print(actions[-1])