class Pawnblack:
    #same general structure for all pieces

    col = "black"
    
    def __init__(self, x, y, move, first, eat):
        self.x = x
        self.y = y
        self.move = move
        self.first = first
        self.eat = eat
        
        
    #rules for movement
    def check(self, a, b):
        if self.x == a and (self.y + 1) == b:
            return True
        elif self.first:
            if self.x == a and (self.y + 2) == b:
                return True
        else:
            return False
        
    def check2(self, a, b):
        if (self.x + 1) == a and (self.y + 1) == b:
            return True
        elif self.x - 1 == a and (self.y + 1) == b:
            return True
        else:
            return False

class Pawnwhite:

    col = "white"

    def __init__(self, x, y, move, first, eat):
        self.x = x
        self.y = y
        self.move = move
        self.first = first
        self.eat = eat
    
    def check(self, a, b):
        if self.x == a and (self.y - 1) == b:
            return True
        elif self.first:
            if self.x == a and (self.y - 2) == b:
                return True
        else:
            return False
        
    def check2(self, a, b):
        if (self.x + 1) == a and (self.y - 1) == b:
            return True
        elif self.x - 1 == a and (self.y - 1) == b:
            return True
        else:
            return False

class Bishop:

    def __init__(self, x, y, move, eat, col):
        self.x = x
        self.y = y
        self.move = move
        self.eat = eat
        self.col = col
    
    def check(self, a, b):
        for i in range(-7, 8):
            if (self.x - a == self.y - b):
                return True
            elif (a == self.x + i) and b == (self.y - i):
                return True
        return False

class Rook:
    
    def __init__(self, x, y, move, eat, col):
        self.x = x
        self.y = y
        self.move = move
        self.eat = eat
        self.col = col
    
    def check(self, a, b):
        if self.x == a and self.y != b:
            return True
        elif self.y == b and self.x != a:
            return True
        else:
            return False
        
class Knight:
    
    def __init__(self, x, y, move, eat, col):
        self.x = x
        self.y = y
        self.move = move
        self.eat = eat
        self.col = col
    
    def check(self, a, b):
        if self.x + 2 == a:
            if self.y + 1 == b or self.y - 1 == b:
                return True
        if self.x - 2 == a:
            if self.y + 1 == b or self.y - 1 == b:
                return True
        if self.y + 2 == b:
            if self.x + 1 == a or self.x - 1 == a:
                return True
        if self.y - 2 == b:
            if self.x + 1 == a or self.x - 1 == a:
                return True
        return False
    
class Queen:
    def __init__(self, x, y, move, eat, col):
        self.x = x
        self.y = y
        self.move = move
        self.eat = eat
        self.col = col
    
    def check(self, a, b):
        if self.x == a and self.y != b:
            return True
        elif self.y == b and self.x != a:
            return True
        for i in range(-7, 8):
            if (self.x - a == self.y - b):
                return True
            elif (a == self.x + i) and b == (self.y - i):
                return True
        return False

class King:
     
    def __init__(self, x, y, move, eat, first, col):
        self.x = x
        self.y = y
        self.move = move
        self.eat = eat
        self.first = first
        self.col = col
    
    def check(self, a, b):
        if (self.x + 1 == a or self.x - 1 == a or self.x == a) and (self.y + 1 == b or self.y - 1 == b or self.y == b) and not (self.x == a and self.y == b):
            return True
        return False   
        

    
def collision(a, b, piece):
    global pieces
    #checks if piece passes over another piece
    
    for n in range(len(pieces)):
        #horizontal
        if piece.x == a:
            if piece.y <= b:
                for m in range(piece.y+1, b, 1):
                    for n in range(len(pieces)):
                        if (pieces[n] != piece) and pieces[n].y == m and pieces[n].x == a:
                            return False
            if piece.y >= b:
                for m in range(b+1, piece.y, 1):
                    for n in range(len(pieces)):
                        if (pieces[n] != piece) and pieces[n].y == m and pieces[n].x == a:
                            return False
        #vertical
        if piece.y == b:
            if piece.x <= a:
                for m in range(piece.x+1, a, 1):
                    for n in range(len(pieces)):
                        if (pieces[n] != piece) and pieces[n].x == m and pieces[n].y == b:
                            return False
            if piece.x >= a:
                for m in range(a+1, piece.x, 1):
                    for n in range(len(pieces)):
                        if (pieces[n] != piece) and pieces[n].x == m and pieces[n].y == b:
                            return False
                            
        p1 = list()
        p2 = list()
        #diagonal
        if piece.x - a == piece.y - b:
            if piece.x >= a and piece.y >= b:
                for m in range(a+1, piece.x, 1):
                    p1.append(m)
                for u in range(b+1, piece.y):
                    p2.append(u)
                for p in range(len(p1)):
                    for n in range(len(pieces)):
                        if (pieces[n] != piece) and pieces[n].x == p1[p] and pieces[n].y == p2[p]:
                            return False
            if piece.x <= a and piece.y <= b:
                for m in range(piece.x, a, 1):
                    p1.append(m)
                for u in range(piece.y, b):
                    p2.append(u)
                for p in range(len(p1)):
                    for n in range(len(pieces)):
                        if (pieces[n] != piece) and pieces[n].x == p1[p] and pieces[n].y == p2[p]:
                            return False
        #diagonal2
        if piece.x >= a and piece.y >= b:
            for m in range(a+1, piece.x, 1):
                p1.append(m)
            for u in range(b+1, piece.y):
                p2.append(u)
            for p in range(len(p1)):
                for n in range(len(pieces)):
                    if (pieces[n] != piece) and pieces[n].x == p1[p] and pieces[n].y == p2[p]:
                        return False
                    
        if piece.x <= a and piece.y <= b:
            for m in range(piece.x+1, a):
                    p1.append(m)
            for u in range(piece.y+1, b):
                p2.append(u)
            for p in range(len(p1)):
                for n in range(len(pieces)):
                    if (pieces[n] != piece) and pieces[n].x == p1[p] and pieces[n].y == p2[p]:
                        return False
            
        return True
    
def moving(a, b):
    #checks if move is valid @ updates pieces
    global turn
    global pieces
    global pieces2
    
    pieces2 = pieces
    
    out = False
    pawncap = False
    collide = False
    check = False
    castle = True
    kinglist = list()
    matelist = list()
    matepiece = list()

    
    for i in range(len(pieces)):
        if pieces[i].move == True:
            lastx = pieces[i].x
            lasty = pieces[i].y
            
            
            #basic check for a vaild square
            if pieces[i].check(a, b) and (pieces[i].x != a or pieces[i].y != b):
                good = True
            else:
                good = False
                
            #checks if king is in check
            for n in range(len(pieces)):
                if pieces[n].col == "black":
                    if pieces[n].check(kingw1.x, kingw1.y) and collision(kingw1.x, kingw1.y, pieces[n]):
                        wcheck = True
                        break
                    else:
                        wcheck = False
                        
            for n in range(len(pieces)):
                if pieces[n].col == "white":
                    if pieces[n].check(kingb1.x, kingb1.y) and collision(kingb1.x, kingb1.y, pieces[n]):
                        bcheck = True
                        break
                    else:
                        bcheck = False

            
            #special code for king(castling/not moving into check)    
            if isinstance(pieces[i], King) == True and pieces[i].col == "white":
                if pieces[i].first == True:
                    if b == pieces[i].y and a == pieces[i].x - 2:
                        if rookw1.x == 0 and rookw1.y == 7:
                            for n in range(len(pieces)):
                                for k in range(3):
                                    if (pieces[n].check(k+1, 7) == True and collision(k+1, 7, pieces[n]) and (pieces[n].col == "black")) or ((pieces[n].x == 1 or pieces[n].x == 2 or pieces[n].x == 3) and pieces[n].y == 7):
                                        castle = False
                                        break
                            if castle:
                                kingw1.x = a
                                rookw1.x = 3
                                castle = True
                                if turn:
                                    turn = False
                                else:
                                    turn = True
                                if kingw1.first == True:
                                    kingw1.first = False
                                    
                    elif b == pieces[i].y and a == pieces[i].x + 2:
                        if rookw2.x == 7 and rookw2.y == 7:
                            for n in range(len(pieces)):
                                for k in range(2):
                                    if (pieces[n].check(k+5, 7) == True and collision(k+5, 7, pieces[n]) and (pieces[n].col == "black")) or ((pieces[n].x == 5 or pieces[n].x == 6) and pieces[n].y == 7):
                                        castle = False
                                        break

                            if castle:
                                kingw1.x = a
                                rookw2.x = 5
                                castle = True
                                if turn:
                                    turn = False
                                else:
                                    turn = True                            
                                if kingw1.first == True:
                                    kingw1.first = False
                    
                            
                            
                            
            if isinstance(pieces[i], King) == True and pieces[i].col == "black":
                if pieces[i].first == True:
                    if b == pieces[i].y and a == pieces[i].x - 2:
                        if rookb1.x == 0 and rookb1.y == 0:
                            for n in range(len(pieces)):
                                for k in range(2):
                                    if (pieces[n].check(k+1, 0) == True and collision(k+1, 0, pieces[n]) and (pieces[n].col == "white")) or ((pieces[n].x == 1 or pieces[n].x == 2 or pieces[n].x == 3) and pieces[n].y == 0):
                                        castle = False
                                        break
                            if castle:
                                kingb1.x = a
                                rookb1.x = 3
                                castle = True
                                if turn:
                                    turn = False
                                else:
                                    turn = True
                                if kingb1.first == True:
                                    kingb1.first = False
                                    
                    elif b == pieces[i].y and a == pieces[i].x + 2:
                        if rookb2.x == 7 and rookb2.y == 0:
                            for n in range(len(pieces)):
                                for k in range(2):
                                    if (pieces[n].check(k+5, 0) == True and collision(k+5, 0, pieces[n]) and (pieces[n].col == "white")) or ((pieces[n].x == 5 or pieces[n].x == 6) and pieces[n].y == 0):
                                        castle = False
                                        break

                            if castle:
                                kingb1.x = a
                                rookb2.x = 5
                                castle = True
                                if turn:
                                    turn = False
                                else:
                                    turn = True
                                if kingb1.first == True:
                                    kingb1.first = False


            

            
                                    
            
            #checks collision
            if good:
                if not collision(a, b, pieces[i]):
                    good = False
                

            
            #special code for pawn(cuz they do weird things)
            if isinstance(pieces[i], Pawnblack) or isinstance(pieces[i], Pawnwhite):
                if good:
                    pieces[i].first = False
                pawncap = pieces[i].check2(a, b)

                
            for n in range(len(pieces)):
                #checks if captured another piece                 
                if (good or pawncap) and (pieces[n] != pieces[i]) and (pieces[n].x == a) and (pieces[n].y == b):
                    collide = True
                    if pieces[i].col == pieces[n].col:
                        good = False
                        pieces[i].move = False
                        break
                    else:
                        pieces[i].move = False
                        #special for pawns
                        if isinstance(pieces[i], Pawnblack) or isinstance(pieces[i], Pawnwhite):
                            if pawncap == True:
                                pieces[i].x = a
                                pieces[i].y = b
                                pieces[i].move = False 
                                pieces[n].eat = True
                                pieces[i].first = False
                                if turn:
                                    turn = False
                                else:
                                    turn = True
                        else:
                            pieces[i].x = a
                            pieces[i].y = b
                            pieces[i].move = False 
                            pieces[n].eat = True
                            if turn:
                                turn = False
                            else:
                                turn = True
                        good = False
                        break 

            
            
            #if no piece is captured
            if good and pieces[i].move == True and not collide:
                if turn:
                    turn = False
                else:
                    turn = True
                pieces[i].x = a
                pieces[i].y = b
                pieces[i].move = False   
            else:
                pieces[i].move = False
            
            
            #prevents king from going into check
            if isinstance(pieces[i], King) == True and pieces[i].col == "white" and (pieces[i].x != a and pieces[i].y != b): 
                for n in range(len(pieces)):
                    if pieces[n].col == "black":
                        print(pieces[n].check(a, b), collision(a, b, pieces[n]), (pieces[n].x == a and pieces[n].y == b))
                        if pieces[n].check(a, b) and collision(a, b, pieces[n]) and not (pieces[n].x == a and pieces[n].y == b):
                            kingw1.x = lastx
                            kingw1.y = lasty
                            if turn:
                                turn = False
                            else:
                                turn = True
                                
            if isinstance(pieces[i], King) == True and pieces[i].col == "black" and (pieces[i].x != a and pieces[i].y != b): 
                for n in range(len(pieces)):
                    if pieces[n].col == "white":
                        if pieces[n].check(a, b) and collision(a, b, pieces[n]) and not (pieces[n].x == a and pieces[n].y == b):
                            kingb1.x = lastx
                            kingb1.y = lasty
                            if turn:
                                turn = False
                            else:
                                turn = True
                                
            
            #prevent other pieces from moving when king is in check
            if isinstance(pieces[i], King) == False and pieces[i].col == "white" and not (lastx == a and lasty == b) and wcheck:
                for n in range(len(pieces)):
                    if pieces[n].col == "black":
                        if pieces[n].check(kingw1.x, kingw1.y) and collision(kingw1.x, kingw1.y, pieces[n]):
                            pieces[i].x = lastx
                            pieces[i].y = lasty
                            for p in range(len(pieces)):
                                if pieces[p].eat == True:
                                    pieces[p].eat == False
                            turn = True
                            
            if isinstance(pieces[i], King) == False and pieces[i].col == "black" and not (lastx == a and lasty == b) and bcheck:
                for n in range(len(pieces)):
                    if pieces[n].col == "white":
                        if pieces[n].check(kingb1.x, kingb1.y) and collision(kingb1.x, kingb1.y, pieces[n]):
                            pieces[i].x = lastx
                            pieces[i].y = lasty
                            for p in range(len(pieces)):
                                if pieces[p].eat == True:
                                    pieces[p].eat == False
                            turn = False


                            


def setup():
    global pawnb
    global pawnw
    global pawn1b
    global pawn1w
    global pieces
    global turn
    global win
    global pawnsb
    global pawnsw
    
    global piecesdraw
    
    global bishopw
    global bishop1w
    global bishop2w
    
    global bishopb
    global bishop1b
    global bishop2b
    
    global rookw
    global rookw1
    global rookw2
    
    global rookb
    global rookb1
    global rookb2
    
    global knightb
    global knightb1
    global knightb2

    global knightw
    global knightw1
    global knightw2
    
    global queenw
    global queenw1
    global queenb
    global queenb1
    
    global kingw
    global kingw1
    global kingb
    global kingb1
    
    size(800, 800)
    textMode(SHAPE)
    turn = True
    win = 0
    pieces2 = list()
    
    
    #all shapes for pieces
    pawnb = createShape(GROUP)
    pawn1 = createShape(ELLIPSE, 50, 30, 35, 35)
    pawn1.setFill(color(0))
    pawn2 = createShape(TRIANGLE, 50, 20, 20, 90, 80, 90)
    pawn2.setFill(color(0))
    pawnb.addChild(pawn2)
    pawnb.addChild(pawn1)
    
    pawnw = createShape(GROUP)
    pawn1 = createShape(ELLIPSE, 50, 30, 35, 35)
    pawn1.setFill(color(255))
    pawn2 = createShape(TRIANGLE, 50, 20, 20, 90, 80, 90)
    pawn2.setFill(color(255))
    pawnw.addChild(pawn2)
    pawnw.addChild(pawn1)
    
    bishopw = createShape(GROUP)
    bishop3 = createShape(TRIANGLE, 30, 85, 70, 85, 50, 10)
    bishop3.setFill(color(255))
    bishopw.addChild(bishop3)
    bishop2 = createShape(ELLIPSE, 50, 20, 25, 25)
    bishop2.setFill(color(255))
    bishopw.addChild(bishop2)
    bishop1 = createShape(RECT, 35, 40, 30, 10)
    bishop1.setFill(color(255))
    bishopw.addChild(bishop1)
    
    bishopb = createShape(GROUP)
    bishop3 = createShape(TRIANGLE, 30, 85, 70, 85, 50, 10)
    bishop3.setFill(color(0))
    bishopb.addChild(bishop3)
    bishop2 = createShape(ELLIPSE, 50, 20, 25, 25)
    bishop2.setFill(color(0))
    bishopb.addChild(bishop2)
    bishop1 = createShape(RECT, 35, 40, 30, 10)
    bishop1.setFill(color(0))
    bishopb.addChild(bishop1)
    
    rookw = createShape(GROUP)
    rook1 = createShape(RECT, 25, 20, 50, 70)
    rook1.setFill(color(255))
    rookw.addChild(rook1)
    rook2 = createShape(RECT, 15, 10, 70, 20)
    rook2.setFill(color(255))
    rookw.addChild(rook2)
    
    rookb = createShape(GROUP)
    rook1 = createShape(RECT, 25, 20, 50, 70)
    rook1.setFill(color(0))
    rookb.addChild(rook1)
    rook2 = createShape(RECT, 15, 10, 70, 20)
    rook2.setFill(color(0))
    rookb.addChild(rook2)
    
    knightw = createShape(GROUP)
    knight1 = createShape(TRIANGLE, 50, 20, 20, 90, 80, 90)
    knight1.setFill(color(255))
    knightw.addChild(knight1)
    knight2 = createShape(TRIANGLE, 15, 25, 75, 5, 75, 45)
    knight2.setFill(color(255))
    knightw.addChild(knight2)
    
    knightb = createShape(GROUP)
    knight1 = createShape(TRIANGLE, 50, 20, 20, 90, 80, 90)
    knight1.setFill(color(0))
    knightb.addChild(knight1)
    knight2 = createShape(TRIANGLE, 15, 25, 75, 5, 75, 45)
    knight2.setFill(color(0))
    knightb.addChild(knight2)
    
    queenw = createShape(GROUP)
    queen1 = createShape(TRIANGLE, 30, 85, 70, 85, 50, 10)
    queen1.setFill(color(255))
    queenw.addChild(queen1)
    queen2 = createShape(TRIANGLE, 50, 5, 40, 25, 60, 25)
    queen2.setFill(color(255))
    queenw.addChild(queen2)
    
    queenb = createShape(GROUP)
    queen1 = createShape(TRIANGLE, 30, 85, 70, 85, 50, 10)
    queen1.setFill(color(0))
    queenb.addChild(queen1)
    queen2 = createShape(TRIANGLE, 50, 5, 40, 25, 60, 25)
    queen2.setFill(color(0))
    queenb.addChild(queen2)
    
    kingb = createShape(GROUP)
    king1 = createShape(TRIANGLE, 30, 85, 70, 85, 50, 10)
    king1.setFill(color(0))
    kingb.addChild(king1)
    king2 = createShape(RECT, 35, 20, 30, 10)
    king2.setFill(color(0))
    kingb.addChild(king2)
    
    kingw = createShape(GROUP)
    king1 = createShape(TRIANGLE, 30, 85, 70, 85, 50, 10)
    king1.setFill(color(255))
    kingw.addChild(king1)
    king2 = createShape(RECT, 35, 20, 30, 10)
    king2.setFill(color(255))
    kingw.addChild(king2)
    


    pieces = list()
    pawnsb = list()
    pawnsw = list()
    piecesdraw = list()
    

    #initilizing opjects

    pawn1b = Pawnblack(1, 1, False, True, False)
    pieces.append(pawn1b)
    pawnsb.append(pawn1b)
    pawn2b = Pawnblack(2, 1, False, True, False)
    pieces.append(pawn2b)
    pawnsb.append(pawn2b)
    pawn3b = Pawnblack(3, 1, False, True, False)
    pieces.append(pawn3b)
    pawnsb.append(pawn3b)
    pawn4b = Pawnblack(4, 1, False, True, False)
    pieces.append(pawn4b)
    pawnsb.append(pawn4b)
    pawn5b = Pawnblack(5, 1, False, True, False)
    pieces.append(pawn5b)
    pawnsb.append(pawn5b)
    pawn6b = Pawnblack(6, 1, False, True, False)
    pieces.append(pawn6b)
    pawnsb.append(pawn6b)
    pawn7b = Pawnblack(7, 1, False, True, False)
    pieces.append(pawn7b)
    pawnsb.append(pawn7b)
    pawn0b = Pawnblack(0, 1, False, True, False)
    pieces.append(pawn0b)
    pawnsb.append(pawn0b)
    
    pawn1w = Pawnwhite(1, 6, False, True, False)
    pieces.append(pawn1w)
    pawnsw.append(pawn1w)
    pawn2w = Pawnwhite(2, 6, False, True, False)
    pieces.append(pawn2w)
    pawnsw.append(pawn2w)
    pawn3w = Pawnwhite(3, 6, False, True, False)
    pieces.append(pawn3w)
    pawnsw.append(pawn3w)
    pawn4w = Pawnwhite(4, 6, False, True, False)
    pieces.append(pawn4w)
    pawnsw.append(pawn4w)
    pawn5w = Pawnwhite(5, 6, False, True, False)
    pieces.append(pawn5w)
    pawnsw.append(pawn5w)
    pawn6w = Pawnwhite(6, 6, False, True, False)
    pieces.append(pawn6w)
    pawnsw.append(pawn6w)
    pawn7w = Pawnwhite(7, 6, False, True, False)
    pieces.append(pawn7w)
    pawnsw.append(pawn7w)
    pawn0w = Pawnwhite(0, 6, False, True, False)
    pieces.append(pawn0w)
    pawnsw.append(pawn0w)
    
    
    
    bishop1w = Bishop(5, 7, False, False, "white")
    pieces.append(bishop1w)
    bishop2w = Bishop(2, 7, False, False, "white")
    pieces.append(bishop2w)
    
    bishop1b = Bishop(5, 0, False, False, "black")
    pieces.append(bishop1b)
    bishop2b = Bishop(2, 0, False, False, "black")
    pieces.append(bishop2b)
    
    piecesdraw.append(bishopw)
    piecesdraw.append(bishop1w)
    piecesdraw.append(bishop2w)
    piecesdraw.append(bishopb)
    piecesdraw.append(bishop1b)
    piecesdraw.append(bishop2b)
    


    
    rookw1 = Rook(0, 7, False, False, "white")
    pieces.append(rookw1)
    rookw2 = Rook(7, 7, False, False, "white")
    pieces.append(rookw2)
    
    rookb1 = Rook(0, 0, False, False, "black")
    pieces.append(rookb1)
    rookb2 = Rook(7, 0, False, False, "black")
    pieces.append(rookb2)
    
    piecesdraw.append(rookw)
    piecesdraw.append(rookw1)
    piecesdraw.append(rookw2)
    piecesdraw.append(rookb)
    piecesdraw.append(rookb1)
    piecesdraw.append(rookb2)
    

    

    
    knightw1 = Knight(1, 7, False, False, "white")
    pieces.append(knightw1)
    knightw2 = Knight(6, 7, False, False, "white")
    pieces.append(knightw2)
    
    knightb1 = Knight(1, 0, False, False, "black")
    pieces.append(knightb1)
    knightb2 = Knight(6, 0, False, False, "black")
    pieces.append(knightb2)
    
    piecesdraw.append(knightw)
    piecesdraw.append(knightw1)
    piecesdraw.append(knightw2)
    piecesdraw.append(knightb)
    piecesdraw.append(knightb1)
    piecesdraw.append(knightb2)
    

    


    queenw1 = Queen(3, 7, False, False, "white")
    pieces.append(queenw1)

    queenb1 = Queen(3, 0, False, False, "black")
    pieces.append(queenb1)

    
    kingw1 = King(4, 7, False, False, True, "white")
    pieces.append(kingw1)
    
    kingb1 = King(4, 0, False, False, True, "black")
    pieces.append(kingb1)


def draw():
    background(139,69,19)
    #draws board
    for i in range(8):
        for x in range(4):
            fill(245,222,179)
            square(0 + 100 * i, 100 + 200 * x - 100 * (i%2), 100)
            
            
    global pawnb
    global pawnw
    global pieces
    global pieces2
    global turn
    global win
    global pawnsb
    global pawnsw
    
    global piecesdraw
    
    global bishopw
    global bishop1w
    global bishop2w
    
    global rookw
    global rookw1
    global rookw2
    
    global rookb
    global rookb1
    global rookb2
    
    global knightb
    global knightb1
    global knightb2

    global knightw
    global knightw1
    global knightw2
    
    global queenw
    global queenw1
    
    global queenb
    global queenb1
    
    global kingw
    global kingw1
    global kingb
    global kingb1
    
    textSize(100)
    if win == 1:
        fill(0)
        text("Black wins", 160, 400)
    elif win == 2:
        fill(255)
        text("White wins", 160, 400)
    else:
        #draws all pieces
        for i in range(len(pawnsb)):
            if pawnsb[i].move == False and pawnsb[i].eat == False:
                shape(pawnb, pawnsb[i].x*100, pawnsb[i].y*100)
        for i in range(len(pawnsw)):
            if pawnsw[i].move == False and pawnsw[i].eat == False:
                shape(pawnw, pawnsw[i].x*100, pawnsw[i].y*100)
                
        for i in range(0, len(piecesdraw), 3):
            if piecesdraw[i+1].move == False and piecesdraw[i+1].eat == False:
                shape(piecesdraw[i], piecesdraw[i+1].x*100, piecesdraw[i+1].y*100)
            if piecesdraw[i+2].move == False and piecesdraw[i+2].eat == False:
                shape(piecesdraw[i], piecesdraw[i+2].x*100, piecesdraw[i+2].y*100)
                
    
        if queenw1.move == False and queenw1.eat == False:
                shape(queenw, queenw1.x*100, queenw1.y*100)
    
                
        if queenb1.move == False and queenb1.eat == False:
                shape(queenb, queenb1.x*100, queenb1.y*100)
                
        if kingw1.move == False and kingw1.eat == False:
                shape(kingw, kingw1.x*100, kingw1.y*100)
                
        if kingb1.move == False and kingb1.eat == False:
                shape(kingb, kingb1.x*100, kingb1.y*100)                 
        
        
        if mousePressed:
            other = True
            a = mouseX//100
            b = mouseY//100
            for n in range(len(pieces)):
                #prevents picking up multiple pieces
                if pieces[n].move == True:
                    other = False
            if other:
                #picks up piece
                for i in range(len(pieces)):
                    if pieces[i].x == a and pieces[i].y == b:
                        if (pieces[i].col == "white") and turn:
                            pieces[i].move = True
                        elif (pieces[i].col == "black") and (not turn):
                            pieces[i].move = True
        
        #draws pieces when they're being moved
        for i in range(len(pawnsb)):            
            if pawnsb[i].move == True and pawnsb[i].eat == False:
                shape(pawnb, mouseX - 40, mouseY - 40)
        for i in range(len(pawnsw)):
            if pawnsw[i].move == True and pawnsw[i].eat == False:
                shape(pawnw, mouseX - 40, mouseY - 40)
        
        
        for i in range(0, len(piecesdraw), 3):    
            if piecesdraw[i+1].move == True and piecesdraw[i+1].eat == False:
                shape(piecesdraw[i], mouseX - 40, mouseY - 40)
            if piecesdraw[i+2].move == True and piecesdraw[i+2].eat == False:
                shape(piecesdraw[i], mouseX - 40, mouseY - 40)
        

        if queenw1.move == True and queenw1.eat == False:
            shape(queenw, mouseX - 40, mouseY - 40)
    
        if queenb1.move == True and queenb1.eat == False:
            shape(queenb, mouseX - 40, mouseY - 40)
        
        if kingw1.move == True and kingw1.eat == False:
            shape(kingw, mouseX - 40, mouseY - 40)
        
        if kingb1.move == True and kingb1.eat == False:
            shape(kingb, mouseX - 40, mouseY - 40)                
        
        
        if not mousePressed:
            a = mouseX//100
            b = mouseY//100
            #moves piece when dropped
            moving(a, b)
            
            #removes eaten pieces from list
            pieces3 = list()
            for i in range(len(pieces)):
                if pieces[i].eat == False:
                    pieces3.append(pieces[i])
            pieces = pieces3
            
            
            #attempted checkmate codes
            
            #lags & false positives
            '''
            if frameCount % 60 == 0:
                for m in range(8):
                    for n in range(8):
                        for i in range(len(pieces)):
                            if pieces[i].col == "white":
                                print(pieces[i], m, n)
                                pieces[i].move = True
                                moving(m, n)
            '''
                            
            
                
                
            
            
            #doesn't cover all cases                            
            '''
            for v in range(kingw1.x-1, kingw1.x+2):
                for w in range(kingw1.y-1, kingw1.y+2):
                    if v >= 0 and w >= 0 and v <= 7 and w <= 7:
                        kinglist.append([v, w])
            
            for m in range(len(kinglist)):
                for n in range(len(pieces)):
                    if ((pieces[n].check(kinglist[m][0], kinglist[m][1]) and collision(kinglist[m][0], kinglist[m][1], pieces[n]) and pieces[n].col == "black") or (pieces[n].col == "white" and pieces[n].x == kinglist[m][0] and pieces[n].y == kinglist[m][1]) and not isinstance(pieces[n], King)):
                        for j in range(len(pieces)):
                            if pieces[n].col == "black" and (pieces[j].check(pieces[n].x, pieces[n].y) and collision(pieces[n].x, pieces[n].y, pieces[j]) and pieces[j].col == "white"):
                                print(pieces[n], pieces[j])
                                matepiece.append(kinglist[m])
                                break
                        matelist.append(kinglist[m])
                        
            print(matepiece)
            print(matelist)
            
            for m in range(len(matepiece)):
                matelist.remove(matepiece[m])
            
            print(matelist)
                    
            if len(kinglist) == len(matelist):
                    win = 1
            '''

                                        
                                        
                                        
                                        
                    
        
                                
                        
            
                            
                
            
                                    
