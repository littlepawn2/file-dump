from Population import Population

class Obst:
    
    def __init__(self, pos, sizex, sizey):
        self.pos = pos
        self.sizex = sizex
        self.sizey = sizey
    
    def show(self):
        rect(self.pos.x, self.pos.y, self.sizex, self.sizey)
        
    def check(self, things):
        for i in things.dots:
            if (i.pos.x > self.pos.x) and (i.pos.y > self.pos.y) and (i.pos.x < self.pos.x + self.sizex) and (i.pos.y < self.pos.y + self.sizey):
                i.dead = True
    
