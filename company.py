worker = {}

class Worker:
    def __init__(self, worker=[], name="Unknown Name"):
        self.worker = worker
        self.name = name

    def getWorker(self):
        return self.worker
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def addWorker(self, worker):
        self.worker.append(worker)


def tree(dict, id):
    try:
        id_infor = dict[id]
        tree_dict = [id]
        for i in id_infor.getWorker():
            tree_dict = tree_dict + tree(dict, i.split(" ", 1)[0])
        return tree_dict
    except Exception:
        return [id]
while True:
    boss = input().split(" ", 1)
    subordinates = input()
    if boss[0] == "END":
        if not subordinates.isdigit():
            for id, item in worker.items():
                if item.getName() == subordinates:
                    subordinates = id
                    break
        print_tree = tree(worker, subordinates)
        print_tree.pop(0)
        for i in sorted(print_tree):
            print(i)
        break
    else:
        if boss[0] not in worker.keys():
            if len(boss) > 1:
                w = Worker([subordinates], boss[1])
                worker[boss[0]] = w
            else:
                worker[boss[0]] = Worker([subordinates])
        else:
            worker[boss[0]].addWorker(subordinates)
