from pgl import GWindow, GOval
import random

def rand_color():
    new="#"
    for i in range (6):
        new+=random.randint(0,9)

size=6

class firework:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.obj=GOval(self.x-size/2,self.y-size/2,size,size)
        self.angle=random.randint(60,120)
        self.travel_length=random.randint(100,200)
        self.explode_size=random.randint()
        self.color=rand_color()
        self.mode=0
