import pygame
import random
import time
from vector import *
from ball import *
from constant import SCREEN_SIZE, Running, screen

global clock
global clock2

def from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb  





def simulation(keys, mousestate):
    global clock
    global clock2
    balls.update()


    if True in mousestate:
        print("clicked")
        ball = balls.tellwitchball(pygame.mouse.get_pos())
        if ball != None and clock2 < timec:
            windows.createwin(ball)
            ball.clicked = Color()
            clock2 = timec + 100
    

    if keys[32] and clock < timec:
        balls.freez = False if balls.freez else True
        clock = timec +  100


windows = Windows()
balls = Balls()
timec = 0
clock = 0
clock2 = 0
for i in range(100):
    balls.newball(i)


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
    time.sleep(.01)
    timec += 1


