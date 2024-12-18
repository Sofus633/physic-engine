import random
import math
import time
from display import * 
from vector import *
from constant import G, SCREEN_SIZE
from color import *
class Ball:
    def __init__(self,num, posvec=None, velo=None, mass=1):
        self.posvec = posvec
        self.velo = velo 
        self.forces = [G]
        self.num = num
        if posvec == None:
            self.posvec = Vector2( random.randint(10,  SCREEN_SIZE[0]-10), random.randint(10, SCREEN_SIZE[1]-10) )
        if velo == None:
            self.velo = Vector2(1, random.randint(-1, 1))
        self.mass = mass 
        self.color = Color()
        self.freez = False
        self.size = 10

    def update(self):
        self.color.set(math.sqrt(self.velo.x**2 + self.velo.y**2) * 100)
        for force in self.forces:
            self.velo += force

        newpos = self.posvec + self.velo
        if newpos.x > SCREEN_SIZE[0] - self.size or newpos.x < self.size:
            self.velo.x = -self.velo.x * .8
        if newpos.y > SCREEN_SIZE[1] - self.size or newpos.y < self.size:
            self.velo.y = -self.velo.y * .8

        if not self.freez:
            self.posvec = self.posvec + self.velo


class Balls:

    def __init__(self):

        self.balls = []

        self.freez = False



    def update(self):

        if self.freez == False:

            self.checkcollition()

        for ball in self.balls:

            if self.freez == False:

                ball.update()

            drawball(ball)

        

    def newball(self, num):

        self.balls.append(Ball(num, velo=Vector2(random.randint(-5, 5), random.randint(-5, 5))))



    def createball(self, num , pos=Vector2(), velo=Vector2(), mass=1):

        self.balls.append(Ball(num, pos, velo, mass))

    

    def checkcollition(self):

        for i in range(len(self.balls)):

            for y in range(i+1, len(self.balls)):

                distance = math.sqrt(

                    (self.balls[i].posvec.x - self.balls[y].posvec.x)**2 +

                    (self.balls[i].posvec.y - self.balls[y].posvec.y)**2

                )

                if distance < self.balls[i].size +  self.balls[y].size:

                    collition(self.balls[i], self.balls[y])

    

    def tellwitchball(self, pos):

        for i in range(len(self.balls)):

            distance = math.sqrt(

                (self.balls[i].posvec.x - pos[0])**2 +

                (self.balls[i].posvec.y - pos[1])**2

            )

            if distance < self.balls[i].size:

                ball = self.balls[i]
                
                
                return ball 
        return None



def collition(ball1, ball2):
    m1 = ball1.mass
    m2 = ball2.mass
    v1 = ball1.velo
    v2 = ball2.velo
    
    v1_final = v1 * (m1 - m2) / (m1 + m2) +  v2 * 2 * m2 / (m1 + m2) 
    v2_final = v2 * (m2 - m1) / (m1 + m2) + v1 * 2 * m1 / (m1 + m2) 

    
    min_distance = (ball1.size / 2) + (ball2.size / 2)
    dx, dy = ball1.posvec.x- ball2.posvec.x, ball1.posvec.y - ball2.posvec.y
    angle = math.atan2(dy, dx)
    distance = math.sqrt(dx**2 + dy**2)
    

    overlap = min_distance - distance + 10
    if distance == 0:  
        distance = 0.01
    dx /= distance
    dy /= distance

    ball1.posvec += Vector2(dx * overlap / 2, dy * overlap / 2)
    ball2.posvec -= Vector2(dx * overlap / 2, dy * overlap / 2)
  
        

    
    
    ball2.velo = v2_final
    ball1.velo = v1_final
