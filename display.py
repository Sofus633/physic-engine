import pygame
import tkinter as tk
from constant import screen, SCREEN_SIZE

def from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'

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
        self.window.title(f"{ball.num}")
        self.window.geometry('500x500')
        self.canva = tk.Canvas(self.window)
        self.ball = ball
    def update(self):
        self.canva.create_oval(10, 10, 100, 100, width=10, outline=from_rgb(self.ball.color.get()))
        self.canva.grid()
        self.window.update()





def drawball(ball):
    pygame.draw.circle(screen , ball.color.get(), ball.posvec.get(), ball.size)

