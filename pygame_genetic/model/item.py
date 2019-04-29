import random

class Item():
    number = 0
    name = None
    des = None
    pos = [0, 0]
    timer = 0
    gole = False

    def __init__(self, number, name, pos):
        self.number = number
        self.name = name + " To " + str(random.randint(1, 4))
        self.des = random.randint(1, 4)
        self.pos = pos
        self.timer = 0
        self.is_exist = True

    def aging(self):
        self.timer += 1

    def get_des(self):
        return self.des