import pygame
import tkinter as tk
from constant import screen

class Windows:
    def __init__(self):
        self.balls = []
        self.windows = []
    def createwin(self, ball):
        if ball not in self.balls:
            self.windows.append(Window(ball))
    def update(self):
        for window in self.windows:
            window.update()
class Window:
    def __init__(self, ball):
        print(f"window initialised for {ball}")
        self.window = tk.Tk()
        self.ball = ball
    def update(self):
        self.window.update()





def drawball(ball):
    pygame.draw.circle(screen , ball.color.get(), ball.posvec.get(), ball.size)

