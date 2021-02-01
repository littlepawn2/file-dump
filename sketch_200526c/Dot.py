from Brain import Brain

class Dot:
    
    def __init__(self):
        self.dotbrain = Brain(400)
        self.pos = PVector(400, 700)
        self.vel = PVector(0, 0)
        self.acc = PVector(0, 0)
        self.getgoal = False
        self.dead = False
        
    def show(self):
        ellipse(self.pos.x, self.pos.y, 8, 8)
    
    def move(self):
        
        if self.dotbrain.step < len(self.dotbrain.instructions):
            self.acc = self.dotbrain.instructions[self.dotbrain.step]
            self.dotbrain.step += 1
        else:
            self.dead = True
        
        if not self.dead:
            self.vel.add(self.acc)
            self.vel.limit(5)
            self.pos.add(self.vel)
        else:
            self.vel = PVector(0, 0)
    
    def update(self):
        if self.pos.x < 4 or self.pos.y < 4 or self.pos.x > 796 or self.pos.y > 796:
            self.dead = True
        if PVector.dist(self.pos, PVector(400, 50)) <= 9:
            self.getgoal = True
            self.dead = True
            
    def fit(self):
        if self.getgoal == True:
            dotfit = 1/81 + (self.dotbrain.step)/10000
        else:
            dotfit = 1.0/(self.pos.dist(PVector(400, 50)))**2
        return dotfit
