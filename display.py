import pygame
import tkinter as tk
from constant import screen, SCREEN_SIZE
from color import Color
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
            self.windows.append(Window(ball, self))
    def update(self):
        for window in self.windows:
            window.update()
            
class Window:
    def __init__(self, ball, windows):
        print(f"window initialised for {ball}")
        self.windows = windows
        self.ball = ball
        self.window = tk.Tk()
        self.window.title(f"{self.ball.num}")
        self.window.geometry('500x500')
        self.canva = tk.Canvas(self.window)
        self.position = tk.Label(self.window, text=str(self.ball.posvec))
        self.speed = tk.Label(self.window, text=str(self.ball.velo))
        self.rect = pygame.Rect(self.ball.posvec.x -  self.ball.size, self.ball.posvec.y -  self.ball.size, self.ball.size, self.ball.size)
        self.color = Color()
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def on_closing(self):
        self.windows.windows.remove(self)
        self.window.destroy()
        
    def update(self):
        self.rect = pygame.Rect(self.ball.posvec.x -  self.ball.size - 5, self.ball.posvec.y -  self.ball.size - 5, (self.ball.size * 2 )+ 10, (self.ball.size * 2)  + 10)
        if self.ball.clicked != False:
            pygame.draw.rect(screen ,self.color.get(), self.rect, 2)
        self.canva.create_oval(10, 10, 100, 100, width=10, outline=from_rgb(self.ball.color.get()))
        self.speed.config(text=str(self.ball.velo))
        self.position.config(text = str(self.ball.posvec))
        self.position.grid()
        self.canva.grid()
        self.speed.grid()
        self.window.update()





def drawball(ball):
    pygame.draw.circle(screen , ball.color.get(), ball.posvec.get(), ball.size)

