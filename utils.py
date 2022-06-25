class Node:
    def __init__(self, state, parent, action, heuristic, cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.heuristic = heuristic
        self.cost = cost


class Stack:
    def __init__(self):
        self.fringe = []

    def add(self, node):
        self.fringe.append(node)

    def empty(self):
        return len(self.fringe) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty stack")
        else:
            node = self.fringe[-1]
            self.fringe = self.fringe[:-1]
            return node


class Queue(Stack):
    def remove(self):
        if self.empty():
            raise Exception("empty queue")
        else:
            node = self.fringe[0]
            self.fringe = self.fringe[1:]
            return node


def heu(self, node):
    (r1, c1) = node
    (r2, c2) = self.goal
    return abs(r2 - r1) + abs(c2 - c1)


def cost(self, node):
    (r1, c1) = node
    (r2, c2) = self.start
    return abs(r2 - r1) + abs(c2 - c1)


def getMinH(fringe):
    Min = 0
    for i in range(1, len(fringe)):
        if fringe[i].heuristic < fringe[Min].heuristic:
            Min = i
    return Min


def getMinC(fringe):
    Min = 0
    for i in range(1, len(fringe)):
        if fringe[i].cost < fringe[Min].cost:
            Min = i
    return Min


def getMinF(fringe):
    Min = 0
    for i in range(1, len(fringe)):
        if (
            fringe[i].cost + fringe[i].heuristic
            < fringe[Min].cost + fringe[Min].heuristic
        ):
            Min = i
    return Min


def FinalCost(actions):
    cost = 0
    if actions[0] == "up":
        cost += 1
    else:
        cost += 2

    for i in range(1, len(actions)):
        if actions[i] == actions[i - 1]:
            cost += 1
        else:
            cost += 2
    return cost
