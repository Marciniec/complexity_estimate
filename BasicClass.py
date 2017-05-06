from random import randint


class Basic:
    def __init__(self):
        self.l = 0
        self.ok = []
        self.target = 0

    def set_up(self, l):
        self.l = l

    def function(self):
        for i in range(0, self.l):
            for j in range(0,self.l):
                x = j*i

    def cleaning(self):
        return self


print(Basic)
