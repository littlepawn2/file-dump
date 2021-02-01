tri_move = 0
f = 0
q = 1
k = 0
r = 0
right = 0
down = 0

def setup():
    size(800, 600)
    
def draw():
    background(0, 0, 0)
    #removes borders
    noStroke()
    #variables, wooooo!
    global r
    g = 0
    b = 0
    global f
    global q
    global k
    global right
    global down
    
    
    if mousePressed:
        colorMode(RGB)
        #makes ghost flash when "vulnerable ghost" is held
        if mouseX >= 50 and mouseX <= 100 and mouseY >= 50 and mouseY <= 100:
            f = f + 1
            if f > 120:
                if f % 30 == 0:
                    if q == 1:
                        q = 2
                    elif q == 2:
                        q = 1
            if q == 1:
                r = 0
                g = 0
                b = 255
            if q == 2:
                r = 255
                g = 255
                b = 255

            else:
                r = 0
                g = 0
                b = 255
        #the rest of the colours
        elif mouseX >= 50 and mouseX <= 100 and mouseY >= 150 and mouseY <= 200:
            r = 255
            g = 157
            b = 157
        elif mouseX >= 50 and mouseX <= 100 and mouseY >= 250 and mouseY <= 300:
            r = 255
            g = 0
            b = 0
        elif mouseX >= 50 and mouseX <= 100 and mouseY >= 350 and mouseY<= 400:
            r = 0
            g = 255
            b = 255
        elif mouseX >= 50 and mouseX <= 100 and mouseY >= 450 and mouseY<= 500:
            r = 255
            g = 166
            b = 0
        else:
            #rainbow!
            q = 1
            f = 0
            colorMode(HSB)
            r = r + 1
            if r > 255:
                r = 0
            g = 255
            b = 255

    else:
        #other rainbow!
        q = 1
        f = 0
        colorMode(HSB)
        r = r + 1
        if r > 255:
            r = 0
        g = 255
        b = 255
    
    #moves it with buttons
    if keyPressed:
            if key == CODED:
                if keyCode == UP:
                    down -= 5
                if keyCode == DOWN:
                    down += 5
                if keyCode == RIGHT:
                    right += 5
                if keyCode == LEFT:
                    right -= 5
    pushMatrix()
    #translates basically everything
    translate(right, down)
    #colour+mainbody
    fill(r, g, b)
    ellipse(400, 200, 200, 200)
    rect(300, 200, 200, 150)
    
    #moving triangles at bottom
    pushMatrix()
    global tri_move
    translate(-300, 0)
    translate(tri_move, 0)
    triangle(300, 350, 365, 350, 332.5, 375)
    pushMatrix()
    translate(67, 0)
    triangle(300, 350, 365, 350, 332.5, 375)
    translate(67, 0)
    triangle(300, 350, 365, 350, 332.5, 375)
    translate(67, 0)
    triangle(300, 350, 365, 350, 332.5, 375)
    translate(67, 0)
    triangle(300, 350, 365, 350, 332.5, 375)
    translate(67, 0)
    triangle(300, 350, 365, 350, 332.5, 375)
    translate(67, 0)
    triangle(300, 350, 365, 350, 332.5, 375)
    translate(67, 0)
    triangle(300, 350, 365, 350, 332.5, 375)
    popMatrix()
    
    tri_move+=3
    if tri_move >= 268:
        tri_move = 0
    popMatrix()
              
    #black bars to hide excess triangles
    fill(0, 0, 0)
    rect(0, 100, 300, 500)
    rect(500, 100, 400, 500)
    
    #entire block is for eyes and mouth
    blink = False
    if mousePressed:
        if mouseX >= 50 and mouseX <= 100 and mouseY >= 50 and mouseY <= 100:       
            blink = True
        else:
            blink = False
    if not blink:    
        pushMatrix()
        colorMode(RGB)
        translate(350, 200)
        fill(255, 255, 255)
        #the white of the eye
        ellipse(0, 0, 60, 60)
        fill(0, 0, 255)
        #the pupil of the eye/making it follow the mouse
        a = atan2(mouseY-(200+down), mouseX-(350+right))
        rotate(a)
        ellipse(15, 0, 25, 25)
        popMatrix()
        
        #the other eye(same code translated to the right)
        pushMatrix()
        translate(425, 200)
        fill(255, 255, 255)
        ellipse(0, 0, 60, 60)
        fill(0, 0, 255)
        a = atan2(mouseY-(200+down), mouseX-(425+right))
        rotate(a)
        ellipse(15, 0, 25, 25)
        popMatrix()
    else:
        #eyes of blinking ghost
        fill(248, 186, 172)
        ellipse(370, 185, 22, 22)
        ellipse(430, 185, 22, 22)
        pushMatrix()
        translate(325, 0)
        #mouth
        noFill()
        stroke(248, 186, 172)
        strokeWeight(15)
        scale(0.5)
        #mouth is a sine wave
        a = 0.0
        inc = TWO_PI/25.0
        for i in range(0, 305, 4):
            point(i, 550+cos(a)*25.0)
            a = a + inc
        scale(1)
        popMatrix()
    popMatrix()
    
    #buttons + text of buttons
    noStroke()
    fill(255, 255, 255)
    textSize(24)
    textAlign(LEFT, TOP)
    
    fill(0, 0, 255)
    rect(50, 50, 50, 50)
    text("Vulnerable Ghost", 50, 105)
    
    fill(255, 157, 157)
    rect(50, 150, 50, 50)
    text("Pinky", 50, 205)
    
    fill(255, 0, 0)
    rect(50, 250, 50, 50)
    text("Blinky", 50, 305)
    
    fill(0, 255, 255)
    rect(50, 350, 50, 50)
    text("Inky", 50, 405)
    
    fill(255, 166, 0)
    rect(50, 450, 50, 50)
    text("Clyde", 50, 505)
    
    fill(255, 255, 255)
    text("Use arrow keys to move", 450, 450)
    

        

    

"""
#attempt at curves(it didn't work)
        thing = 20
        thing2 = thing*2
        start = 350
        ylevel = 300
        curveheight = 50
        for i in range(5):
            bezier(start+thing, ylevel, start+thing, ylevel-curveheight, start+thing+thing2, ylevel-curveheight, start+thing+thing2, ylevel)
            bezier(start+thing, ylevel, start+thing, ylevel+curveheight, start+thing+thing2, ylevel+curveheight, start+thing+thing2, ylevel)
            bezier(start+thing, ylevel, start+thing, ylevel-curveheight, start+thing+thing2, ylevel-curveheight, start+thing+thing2, ylevel)
            bezier(start+thing, ylevel, start+thing, ylevel+curveheight, start+thing+thing2, ylevel+curveheight, start+thing+thing2, ylevel)
            bezier(start+thing, ylevel, start+thing, ylevel-curveheight, start+thing+thing2, ylevel-curveheight, start+thing+thing2, ylevel)
            thing += 20
"""    
        
def mousePressed():
    println((mouseX,mouseY))
