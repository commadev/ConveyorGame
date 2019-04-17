from model.item import Item
from model.variable import *
import pygame
import sys
import copy

pygame.init()
pygame.display.set_caption("Conveyor Game")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

item = []

for i in range(8):
    if i < 4:
        item.append(Item(i, "Notebook", [MAP_HEIGHT-2, i]))
    else:
        item.append(Item(i, "Notebook", [MAP_HEIGHT-1, i-4]))

item_length = 8
index = 0

def move(key_event):
    global index
    if key_event[pygame.K_LEFT]:
        if item[index].pos[1] > 0:
            if print_map[item[index].pos[0]][item[index].pos[1] - 1] == 0:
                item[index].pos[1] -= 1
            elif print_map[item[index].pos[0]][item[index].pos[1] - 1] == item[index].get_des():
                item[index].gole = True
                for i in range(8):
                    if item[i].number > item[index].number:
                        item[i].number -= 1
                item[index].number = -1
        else:
            item[index].aging()
        index += 1
        if index > item_length - 1:
            index = 0

    if key_event[pygame.K_RIGHT]:
        if item[index].pos[1] < MAP_WIDTH - 1:
            if print_map[item[index].pos[0]][item[index].pos[1] + 1] == 0:
                item[index].pos[1] += 1
            elif print_map[item[index].pos[0]][item[index].pos[1] + 1] == item[index].get_des():
                item[index].gole = True
                for i in range(8):
                    if item[i].number > item[index].number:
                        item[i].number -= 1
                item[index].number = -1
        else:
            item[index].aging()
        index += 1
        if index > item_length - 1:
            index = 0
    
    if key_event[pygame.K_UP]:
        if item[index].pos[0] > 0:
            if print_map[item[index].pos[0] - 1][item[index].pos[1]] == 0:
                item[index].pos[0] -= 1
            elif print_map[item[index].pos[0] - 1][item[index].pos[1]] == item[index].get_des():
                item[index].gole = True
                for i in range(8):
                    if item[i].number > item[index].number:
                        item[i].number -= 1
                item[index].number = -1
        else:
            item[index].aging()
        index += 1
        if index > item_length - 1:
            index = 0

    if key_event[pygame.K_DOWN]:
        if item[index].pos[0] < MAP_HEIGHT - 1:
            if print_map[item[index].pos[0] + 1][item[index].pos[1]] == 0:
                item[index].pos[0] += 1
            elif print_map[item[index].pos[0] + 1][item[index].pos[1]] == item[index].get_des():
                item[index].gole = True
                for i in range(8):
                    if item[i].number > item[index].number:
                        item[i].number -= 1
                item[index].number = -1
        else:
            item[index].aging()
        index += 1
        if index > item_length - 1:
            index = 0

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
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    print_map = copy.deepcopy(map)
    for i in range(8):
        if item[i].gole == False:
            print_map[item[i].pos[0]][item[i].pos[1]] = item[i]
    
    key_event = pygame.key.get_pressed()
    move(key_event)

    screen.fill(BLACK)

    draw_screen()
        
    pygame.display.update()