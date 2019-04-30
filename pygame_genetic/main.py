from model.item import Item
from model.variable import *
import pygame
import sys
import copy
import random

pygame.init()
pygame.display.set_caption("Conveyor Game")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

item = []
index = 0
max_index = 8
remain_item = 0
print_map = []

def item_init():
    global item
    item = []
    for i in range(8):
        if i < 4:
            item.append(Item(i, "Notebook", [MAP_HEIGHT-2, i]))
        else:
            item.append(Item(i, "Notebook", [MAP_HEIGHT-1, i-4]))

def index_up():
    global index
    index += 1
    if index > max_index - 1:
        index = 0

def move(key_event):
    global max_index
    global remain_item

    if item[index].gole == True:
        index_up()
        return
    
    if key_event[pygame.K_LEFT]:
        if item[index].pos[1] > 0:
            if print_map[item[index].pos[0]][item[index].pos[1] - 1] == 0:
                item[index].pos[1] -= 1
        else:
            item[index].aging()
        index_up()

    if key_event[pygame.K_RIGHT]:
        if item[index].pos[1] < MAP_WIDTH - 1:
            if print_map[item[index].pos[0]][item[index].pos[1] + 1] == 0:
                item[index].pos[1] += 1
        else:
            item[index].aging()
        index_up()
    
    if key_event[pygame.K_UP]:
        if item[index].pos[0] > 0:
            if print_map[item[index].pos[0] - 1][item[index].pos[1]] == 0:
                item[index].pos[0] -= 1
            elif print_map[item[index].pos[0] - 1][item[index].pos[1]] == item[index].get_des() and item[index].gole == False:
                item[index].gole = True
                remain_item -= 1
                for i in range(8):
                    if item[i].number > item[index].number:
                        item[i].number -= 1
                item[index].number = -1
        else:
            item[index].aging()
        index_up()

    if key_event[pygame.K_DOWN]:
        if item[index].pos[0] < MAP_HEIGHT - 1:
            if print_map[item[index].pos[0] + 1][item[index].pos[1]] == 0:
                item[index].pos[0] += 1
        else:
            item[index].aging()
        index_up()

def choice_dir(key_event):
    
    a = random.randint(0,100)
    
    if a < 10:
        key_event[pygame.K_DOWN] = 1
        return key_event
    
    if a > 50:
        key_event[pygame.K_UP] = 1
        return key_event
    
    print(str(index)+" - pos : "+str(item[index].pos[1]))
    print(str(index)+" - des : "+str(item[index].des-1))
        
    if item[index].des-1 < item[index].pos[1]:
        key_event[pygame.K_LEFT] = 1
    elif item[index].des-1 > item[index].pos[1]:
        key_event[pygame.K_RIGHT] = 1
    elif item[index].des-1 == item[index].pos[1]:
        key_event[pygame.K_UP] = 1
    return key_event

def draw_screen():
    for i in range(MAP_HEIGHT):
        for j in range(MAP_WIDTH):
            if map[i][j] == 1:
                pygame.draw.rect(screen, RED, [j*RECT_SIZE, i*RECT_SIZE, RECT_SIZE, RECT_SIZE], 0)
            elif map[i][j] == 2:
                pygame.draw.rect(screen, GREEN, [j*RECT_SIZE, i*RECT_SIZE, RECT_SIZE, RECT_SIZE], 0)
            elif map[i][j] == 3:
                pygame.draw.rect(screen, BLUE, [j*RECT_SIZE, i*RECT_SIZE, RECT_SIZE, RECT_SIZE], 0)
            elif map[i][j] == 4:
                pygame.draw.rect(screen, YELLOW, [j*RECT_SIZE, i*RECT_SIZE, RECT_SIZE, RECT_SIZE], 0)
            else:
                pygame.draw.rect(screen, BLACK, [j*RECT_SIZE, i*RECT_SIZE, RECT_SIZE, RECT_SIZE], 0)
    
    for i in range(8):
        if item[i].gole != True:
            if item[i].des == 1:
                pygame.draw.rect(screen, RED, [item[i].pos[1]*RECT_SIZE, item[i].pos[0]*RECT_SIZE, RECT_SIZE, RECT_SIZE], 0)
            elif item[i].des == 2:
                pygame.draw.rect(screen, GREEN, [item[i].pos[1]*RECT_SIZE, item[i].pos[0]*RECT_SIZE, RECT_SIZE, RECT_SIZE], 0)
            elif item[i].des == 3:
                pygame.draw.rect(screen, BLUE, [item[i].pos[1]*RECT_SIZE, item[i].pos[0]*RECT_SIZE, RECT_SIZE, RECT_SIZE], 0)
            elif item[i].des == 4:
                pygame.draw.rect(screen, YELLOW, [item[i].pos[1]*RECT_SIZE, item[i].pos[0]*RECT_SIZE, RECT_SIZE, RECT_SIZE], 0)

clock = pygame.time.Clock()
while True:
    clock.tick(FPS)

    if remain_item <= 0:
        item_init()
        remain_item = 8

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    print_map = copy.deepcopy(map)
    for i in range(8):
        if item[i].gole == False:
            print_map[item[i].pos[0]][item[i].pos[1]] = item[i]
    
    key_event = list(pygame.key.get_pressed())
    key_event = choice_dir(key_event)
    move(key_event)

    screen.fill(BLACK)
    draw_screen()
    pygame.display.update()