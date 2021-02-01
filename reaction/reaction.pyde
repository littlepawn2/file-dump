start = False
first = True
col = 200
counter = 0

def setup():
    size(800, 600)
    frameRate(60)
    textSize(24)
    
def draw():
    global start, first, col, frame, count, counter
    
    background(col)
    
    text("Click mouse to start, press any key after the screen turns white", 0, 200)
    
    if mousePressed:
        start = True
        
    if start and first:
        frame = frameCount
        count = int(random(3, 10))
        col = 0
        first = False
    
    if start:
        
        if frameCount >= frame + count*60:
            col = 255
            counter += 1          
            if keyPressed:
                print(counter/60.0)
                print("{}/60".format(counter))
                exit()
            
        
        
    
    
