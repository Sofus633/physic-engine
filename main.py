import pygame
import random
import time
from vector import *
from ball import *
from constant import SCREEN_SIZE, Running, screen

def simulation(keys, mousestate):

    balls.update()
    if True in mousestate:
        ball = balls.tellwitchball(pygame.mouse.get_pos())
        if ball != None and clock2 < timec:
            windows.createwin(ball)
            print("clicked")
            clock2 = time + 1000
    

    if pygame.K_SPACE in keys and clock < timec:
        balls.freez = False if balls.freez else True
        clock = timec +  1000


windows = Windows()
balls = Balls()
timec = 0

for i in range(100):
    balls.newball(i)
balls.freez = True

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False
    keys = pygame.key.get_pressed() 
    mousestate = pygame.mouse.get_pressed()
    simulation(keys, mousestate)
    windows.update()



    pygame.display.flip()
    screen.fill((200, 200, 200))
    time.sleep(.001)
    timec += 1


