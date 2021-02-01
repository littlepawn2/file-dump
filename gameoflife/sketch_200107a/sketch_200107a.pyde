

class Cell():
    # a single cell
    def __init__(self, x, y, life):
        self.x = x
        self.y = y
        self.life = life
        

def setup():
    global cells, cells2
    
    size(800, 820)
    frameRate(30)
    
    cells = list()
    cells2 = list()

    #initilizing all cells
    for x in range(0, 40):
        for y in range(0, 40):
            cells.append(Cell(x, y, False))
            
            
    #copy of cells        
    cells2 = cells
    


def draw():
    global cells, cells2
    
    background(255)
    fill(0)
    
    #drawing grid
    for x in range(41):
        line(x*20, 0, x*20, 800)
        line(0, x*20, 800, x*20)
        
    #drawing cells    
    for i in cells:
        if i.life == True:
            rect(i.x*20, i.y*20, 20, 20)
    
    
    
    #drawing button
    fill(200)
    rect(500, 800, 160, 20)
    
    fill(0)
    textSize(20)
    text("Next", 550, 818)
    
    if mousePressed:
        #position of mouse(on grid)
        a = mouseX // 20
        b = mouseY // 20
        
        #allows drawing of cells
        for p in range(len(cells)):
            if [cells[p].x, cells[p].y] == [a,b]:
                cells[p].life = True

        #code runs when button is pressed
        #takes about 10s
        if b == 40 and a >= 25 and a <= 33:
            print("hi")
            for i in cells:
            
                surround = []
                surroundcell = []
                livecount = 0
                surx = 0
                sury = 0
                
                #gets position of surrounding cells
                for m in range(-1, 2):
                    for n in range(-1, 2):
                        if i.x+m == 40:
                            surx = 0
                        elif i.x+m == -1:
                            surx = 39
                        else:
                            surx = i.x+m
                        
                        if i.y+n == 40:
                            sury = 0
                        elif i.y+n == -1:
                            sury = 39
                        else:
                            sury = i.y+n
                            
                        surround.append([surx, sury])
                
                #finds which cells are surrounding
                for p in cells:
                    for q in surround:
                        if p != i and [p.x, p.y] == q:
                            surroundcell.append(p)
        
                #counts how many cells are live
                for x in surroundcell:
                        if x.life == True:
                            livecount += 1
                
                #rules for survival/reproduction
                if livecount <= 1 or livecount >= 4:
                    cells2[cells.index(i)].life = False
                elif livecount == 2 and i.life == True:
                    cells2[cells.index(i)].life = True
                elif livecount == 3:
                    cells2[cells.index(i)].life = True

            #updates main cell list
            cells = cells2
            print("bye")


                
                
                
                

                
                
        
        
        
