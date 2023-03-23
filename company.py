worker = {}
#employees = {}

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


def addition(string, dict):
    if len(string) > 1:
        dict[string[0]] = string[1]
    else:
        if string[0] not in employees.keys():
            employees[string[0]] = "Unknown Name"
    return dict

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
            #subordinates = list(employees.keys())[list(employees.values()).index(subordinates)]
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


    #addition(boss, employees)
    #addition(subordinates, employees)




# дана строка которая включает в себя 3 вида скобок, определить правильно ли раставлены скобки (), [], {}
# sortlist, list, словарь, очередь, стек,