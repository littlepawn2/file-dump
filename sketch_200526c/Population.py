from Dot import Dot

class Population:
    
    def __init__(self, number):
        self.dots = list()
        self.number = number
        
        for i in range(self.number):
            self.dots.append(Dot())
    
    def show(self):
        for i in range(self.number):
            self.dots[i].show()
    
    def move(self):
        for i in range(self.number):
            self.dots[i].move()
            
    def update(self):
        for i in range(self.number):
            self.dots[i].update()
            
    def check(self):
        for i in range(self.number):
            if self.dots[i].dead == False:
                return False
        return True
    
    def fitcheck(self):
        fits = list()
        for i in range(self.number):
            fits.append(self.dots[i].fit())
        fits.sort(reverse = True)
        
        #for i in range(10):
            #fits[i] += 0.01
            
        return fits

    def calcfitsum(self):
        fitsum = 0
        for i in self.fitcheck():
            fitsum += i
        return fitsum
    
    def select(self):
        runsum = 0
        fitsum = self.calcfitsum()
        
        for i in range(0, self.number):
            runsum += self.dots[i].fit()
            if runsum > random(0, fitsum):
                return self.dots[i]
            
            
    def natselect(self):
        babies = list()
        for i in range(0, 300):
            baby = Dot()
            parent = self.select()
            baby.dotbrain = baby.dotbrain.clone(parent)
            baby.dotbrain.mutate()
            babies.append(baby)
        
        self.dots = babies

        
        
        
            
        
