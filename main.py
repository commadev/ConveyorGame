import random
import copy
import os
import sys
import tty
import termios


map = [
    [1, 2, 3, 4],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

MAP_HEIGHT = len(map)


class Item():
    number = 0
    name, des = None, None
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


def getch():
    old_settings = termios.tcgetattr(0)
    new_settings = old_settings[:]
    new_settings[3] &= ~termios.ICANON
    try:
        termios.tcsetattr(0, termios.TCSANOW, new_settings)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(0, termios.TCSANOW, old_settings)
    return ch


def draw(item, move_index_count):
    print_map = copy.deepcopy(map)
    for i in range(8):
        if item[i].gole == False:
            print_map[item[i].pos[0]][item[i].pos[1]] = item[i]

    for i in range(MAP_HEIGHT):
        for j in range(4):
            if type(print_map[i][j]) is not Item:
                print(print_map[i][j], end='')
            else:
                print(print_map[i][j].get_des(), end='')
        print()

    for i in range(8):
        if item[i].number == move_index_count:
            x = getch()
            if x == 'w':
                if item[i].pos[0] > 0:
                    if print_map[item[i].pos[0] - 1][item[i].pos[1]] == 0:
                        item[i].pos[0] -= 1
                    elif print_map[item[i].pos[0] - 1][item[i].pos[1]] == item[i].get_des():
                        item[i].gole = True
                        for j in range(8):
                            if item[j].number > item[i].number:
                                item[j].number -= 1
                        item[i].number = -1
                else:
                    item[i].aging()
            elif x == 's':
                if item[i].pos[0] < MAP_HEIGHT - 1:
                    if print_map[item[i].pos[0] + 1][item[i].pos[1]] == 0:
                        item[i].pos[0] += 1
                    elif print_map[item[i].pos[0] + 1][item[i].pos[1]] == item[i].get_des():
                        item[i].gole = True
                        for j in range(8):
                            if item[j].number > item[i].number:
                                item[j].number -= 1
                        item[i].number = -1
                else:
                    item[i].aging()
            elif x == 'a':
                if item[i].pos[1] > 0:
                    if print_map[item[i].pos[0]][item[i].pos[1] - 1] == 0:
                        item[i].pos[1] -= 1
                    elif print_map[item[i].pos[0]][item[i].pos[1] - 1] == item[i].get_des():
                        item[i].gole = True
                        for j in range(8):
                            if item[j].number > item[i].number:
                                item[j].number -= 1
                        item[i].number = -1
                else:
                    item[i].aging()
            elif x == 'd':
                if item[i].pos[1] < 3:
                    if print_map[item[i].pos[0]][item[i].pos[1] + 1] == 0:
                        item[i].pos[1] += 1
                    elif print_map[item[i].pos[0]][item[i].pos[1] + 1] == item[i].get_des():
                        item[i].gole = True
                        for j in range(8):
                            if item[j].number > item[i].number:
                                item[j].number -= 1
                        item[i].number = -1
                else:
                    item[i].aging()

    os.system('cls' if os.name == 'nt' else 'clear')


item = []

for i in range(8):
    if i < 4:
        item.append(Item(i, "Notebook", [MAP_HEIGHT-2, i]))
    else:
        item.append(Item(i, "Notebook", [MAP_HEIGHT-1, i-4]))

move_index_count = 0

while 1:
    draw(item, move_index_count)
    move_index_count += 1
    if move_index_count > 8:
        move_index_count = 0
