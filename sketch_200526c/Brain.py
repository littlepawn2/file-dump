class Brain:

    def __init__(self, listsize):
        self.instructions = list()
        self.step = 0
        for i in range(listsize):
            self.instructions.append(PVector.fromAngle(random(0, TWO_PI)))
    
    def clone(self, parent):
        clone = Brain(len(self.instructions))
        for i in range(len(self.instructions)):
            clone.instructions[i] = parent.dotbrain.instructions[i]
        
        return clone
    
    def mutate(self):
        mutationrate = 0.01
        
        for i in range(len(self.instructions)):
            rand = random(0, 1)
            if rand < mutationrate:
                self.instructions[i] = PVector.fromAngle(random(0, TWO_PI))
