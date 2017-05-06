from math import ceil, floor
from random import randint


class Basic:
    def __init__(self):
        self.l = 0
        self.ok = []
        self.target = 0

    def set_up(self, l):
        self.l = l
        self.ok = list(range(0, l))
        self.target = randint(0, l)

    def function(self):
        p = floor(self.l / 2).__int__()
        if not self.ok:
            return
        if self.ok[p] < self.target:
            p /= 2
        elif self.ok[p] > self.target:
            p = p + floor((len(self.ok) - p) / 2)
        elif self.ok[p] == self.target:
            return

    def cleaning(self):
        return self


print(Basic)
