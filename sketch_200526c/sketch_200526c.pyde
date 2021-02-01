from Population import Population 
from Obst import Obst
from Dot import Dot
        
def setup():
    size(800, 800)
    global test, goal, testdot, gen, obstacle
    test = Population(300)
    testdot = Dot()
    goal = PVector(400, 50)
    obstacle = Obst(PVector(0, 350), 400, 20)
    gen = 1
    
    
def draw():
    global test, goal, testdot, gen, obstacle
    background(0)
    
    fill(color(255, 0, 0))
    text(str(gen), 50, 50)
    ellipse(goal.x, goal.y, 10, 10)
    
    fill(255)
    if test.check() == True:
        gen += 1
        test.natselect()
        for i in test.dots:
            i.dotbrain.mutate()
        print(gen)
    
    obstacle.show()
    obstacle.check(test)
    test.update()
    test.move()
    test.show()
    
