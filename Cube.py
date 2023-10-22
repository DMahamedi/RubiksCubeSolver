import random

class Cube:

    """ 
    DESCRIPTION AND PLANS
    this program includes the basic functionality needed to solve a rubiks cube, including an ability to input
    the cubes current state, the ability to rotate sides and keep track of what happens.
    StandardCube() inherits from this class to solve the cube.
    I plan to implement more sophisticated algorithms than the ones used in StandardCube.py, namely the algorithms listed
    here:
    https://en.wikipedia.org/wiki/Optimal_solutions_for_the_Rubik%27s_Cube#Thistlethwaite's_algorithm
    """

    def __init__(self, white=['w']*9, red=['r']*9, blue=['b']*9, yellow=['y']*9, green=['g']*9, orange=['o']*9):
        self.white = white
        self.red = red
        self.blue = blue
        self.yellow = yellow
        self.green = green
        self.orange = orange

    def getWhite(self): #return white face
        return self.white
    
    def getRed(self): #return red face
        return self.red
    
    def getBlue(self): #return blue face
        return self.blue
    
    def getYellow(self): #return yellow face
        return self.yellow
    
    def getGreen(self): #return green face
        return self.green
    
    def getOrange(self): #return  face
        return self.orange

    def userOperation(self): #allows interactive modification of the cube
        userIn = ""
        while userIn != "q":
            print("ENTER 'q' TO QUIT")
            userIn = input("Enter which face would you like to rotate: ")
            if userIn == 'q':
                break
            numRotations = int(input('Enter number of rotations: '))
            face = self.white
            match userIn:
                case 'white':
                    face = self.white
                case 'blue':
                    face = self.blue
                case 'red':
                    face = self.red
                case 'green':
                    face = self.green
                case 'orange':
                    face = self.orange
                case 'yellow':
                    face = self.yellow
                case other:
                    print('sorry, that face is not recognized')
                    continue
            for i in range(numRotations):
                self.rotateCW(face)
            self.printCube()

    def printFace(self, face): #prints a specified face of the cube
        for i in range(3):
            temp = [' '] * 3 + face[3*i: 3*i+3] + [' '] * 6
            print(temp)

    def printCube(self): #prints the full cube in a nice format
    #note that you can see what 'color' a 9x9 grid is associated to by looking at the character in the middle (index 4)
    #note that that color piece will NEVER move
    #also be aware that this is the format of the cube the program is designed around
    #in other words, each 9x9 grid, top to bottom is oriented how the program treats each face
        self.printFace(self.yellow)
        for i in range(3):
            t = 3*i
            temp = self.blue[t:t+3] + self.red[t:t+3] + self.green[t:t+3] + self.orange[t:t+3]
            print(temp)
        self.printFace(self.white)
        print()
    
    def printCubeImproved(self): # prints cube using full color names instead of abbreviations
        #FIXME: ADD THIS FUNCTIONALITY
        print("FIXME: FUNCTIONALITY NOT YET ADDED")

    def findFace(self, face, side): # given a face (red, white, etc.) and an assiociated side (front, back), returns face occupying that side
        match face:
            case self.white:
                match side:
                    case 'top':
                        return self.red
                    case 'right':
                        return self.green
                    case 'bottom':
                        return self.orange
                    case 'left':
                        return self.blue
                    case 'back':
                        return self.yellow
            case self.red:
                match side:
                    case 'top':
                        return self.yellow
                    case 'right':
                        return self.green
                    case 'bottom':
                        return self.white
                    case 'left':
                        return self.blue
                    case 'back':
                        return self.orange
            case self.green:
                match side:
                    case 'top':
                        return self.yellow
                    case 'right':
                        return self.orange
                    case 'bottom':
                        return self.white
                    case 'left':
                        return self.red
                    case 'back':
                        return self.blue
            case self.blue:
                match side:
                    case 'top':
                        return self.yellow
                    case 'right':
                        return self.red
                    case 'bottom':
                        return self.white
                    case 'left':
                        return self.orange
                    case 'back':
                        return self.green
            case self.yellow:
                match side:
                    case 'top':
                        return self.orange
                    case 'right':
                        return self.green
                    case 'bottom':
                        return self.red
                    case 'left':
                        return self.blue
                    case 'back':
                        return self.white
            case self.orange:
                match side:
                    case 'top':
                        return self.yellow
                    case 'right':
                        return self.blue
                    case 'bottom':
                        return self.white
                    case 'left':
                        return self.green
                    case 'back':
                        return self.red

    def matchColorToFace(self, color): #takes in color abbreviation like 'w' for white and spits back associated face (like 'r' becomes red)
        match color:
            case 'w':
                return self.white
            case 'b':
                return self.blue
            case 'r':
                return self.red
            case 'g':
                return self.green
            case 'o':
                return self.orange
            case 'y':
                return self.yellow
            
    def getFaceRows(self, face, row, reverse=False): #retrieves the faces top or bottom row -- used by findOutterTriplets()
        #t for top and b for bottom
        triplet = []
        if row == 't':
            triplet = [face[0:3],face,'row','t']
        elif row == 'b':
            triplet = [face[6:],face,'row','b']

        if reverse == True:
            triplet[0][0], triplet[0][2] = triplet[0][2], triplet[0][0]
        return triplet
        
    def getFaceCols(self, face, col, reverse=False): #retrieves the faces left or right column -- used by findOutterTriplets()
        #l for left and r for right
        triplet = []
        if col == 'l':
            triplet = [[face[0],face[3],face[6]],face,'column','l']
        elif col == 'r':
            triplet = [[face[2],face[5],face[8]],face,'column','r']

        if reverse == True:
            triplet[0][0], triplet[0][2] = triplet[0][2], triplet[0][0]
        return triplet

    def changeFaceRow(self, face, newRow, row): #changes the appropriate row after a rotation -- used by rotateCW()
        #t for top and b for bottom
        if row == 't':
            face[0:3] = newRow
        elif row == 'b':
            face[6:] = newRow
    
    def changeFaceColumn(self, face, newColumn, col): #changes the appropriate column after a rotation -- used by rotateCW()
        #l for left and r for right
        if col == 'l':
            face[0] = newColumn[0]
            face[3] = newColumn[1]
            face[6] = newColumn[2]
        elif col == 'r':
            face[2] = newColumn[0]
            face[5] = newColumn[1]
            face[8] = newColumn[2]

    def findOutterTriplets(self, frontFace): #used for side cubies that are used rotating a face -- used by rotateCW()
        #find the triplets on the outer edge of the face
        #because the faces are described top to bottom relative to the bottom face
        #the orientation of the cube means that for the program to access the triplets correctly while maintaing proper geometry,
        #it needs to access them differently depending on which 'front face' we are using as a reference
        #i.e. some cublets are part of a row from a different face, while others are part of a column

        #this program handles it on a case by case basis, and for each of the four outter faces,
        #it returns a list triplet containing the three cublets lining the front face, the face the cublets are from
        # and whether they are part of a column (and if its a colun whether its the left or right one)
        # or part of a row (and if its a row then whether its the left or right row) 
        #NOTE: outter faces will always be listed in the clockwise order of
        #topFace, rightFace, bottomFace, leftFace
        if frontFace == self.white: #red, green, orange, blue
            return [self.getFaceRows(self.red,'b'), self.getFaceRows(self.green,'b'), self.getFaceRows(self.orange,'b'), self.getFaceRows(self.blue,'b')]
        elif frontFace == self.blue: #yellow, red, white, orange
            return [self.getFaceCols(self.yellow,'l'), self.getFaceCols(self.red,'l'), self.getFaceCols(self.white,'l',True), self.getFaceCols(self.orange,'r',True)]
        elif frontFace == self.red: #yellow, green, white, blue
            return [self.getFaceRows(self.yellow,'b'), self.getFaceCols(self.green,'l',True), self.getFaceRows(self.white,'t'), self.getFaceCols(self.blue,'r',True)]
        elif frontFace == self.green: #yellow, orange, white, red
            return [self.getFaceCols(self.yellow,'r',True), self.getFaceCols(self.orange,'l',True), self.getFaceCols(self.white,'r'), self.getFaceCols(self.red,'r')]
        elif frontFace == self.yellow: #orange, green, red, blue
            return [self.getFaceRows(self.orange,'t'), self.getFaceRows(self.green,'t'), self.getFaceRows(self.red,'t')   ,self.getFaceRows(self.blue,'t')]
        elif frontFace == self.orange: #yellow, blue, white, green
            return [self.getFaceRows(self.yellow,'t',True), self.getFaceCols(self.blue,'l'), self.getFaceRows(self.white,'b',True), self.getFaceCols(self.green,'r')]

    def rotateCW(self, frontFace): # master function used for all rotations

        triplets = self.findOutterTriplets(frontFace)
        lastTripletOld = triplets[3][0]
        rotatedFace = [0] * 9

        #FIXME: CONSIDER USING A FOR LOOP OR SOMETHING
        rotatedFace[0] = frontFace[6]
        rotatedFace[1] = frontFace[3]
        rotatedFace[2] = frontFace[0]
        rotatedFace[3] = frontFace[7]
        rotatedFace[4] = frontFace[4] #middle stays fixed
        rotatedFace[5] = frontFace[1]
        rotatedFace[6] = frontFace[8]
        rotatedFace[7] = frontFace[5]
        rotatedFace[8] = frontFace[2]

        frontFace[:] = rotatedFace

        for i in range(4):
            newTriplet = [] #the triplet which will be replacing the current one
            tripletFace = triplets[i][1]
            isRowOrCol = triplets[i][2]

            if i == 0: #i = 0 corresponds to the top face, then goes in clockwise order of right, bottom, left
                newTriplet = lastTripletOld #the top face triplet gets updated with left faces (the left face is also the last face)
            else:
                newTriplet = triplets[i-1][0] #otherwise, the new triplet can come from the previous face

            #for changeFaceRow and changeFaceColumn, input is: i) face being updated, ii) the new triplet, and iii) the row/column being updated
            if isRowOrCol == 'row':
                self.changeFaceRow(tripletFace,newTriplet,triplets[i][-1])
            else:
                self.changeFaceColumn(tripletFace,newTriplet,triplets[i][-1])
           
    def rotateCCW(self, frontFace): #rotates CCW using rotateCW three times
        #since rotating CCW is the same as rotating CW 3 times
        self.rotateCW(frontFace)
        self.rotateCW(frontFace)
        self.rotateCW(frontFace)

    def scrambleCube(self, numMoves=25): #scrambles the cube randomly, default of 25 random operations
        face = self.white
        for i in range(numMoves):
            val = random.randint(1,6) #chooses which side to rotate
            match val:
                case 1: #match face to white
                    face = self.white
                case 2: #match face to blue
                    face = self.blue
                case 3: #match face to red
                    face = self.red
                case 4: #match face to green
                    face = self.green
                case 5: #match face to orange
                    face = self.orange
                case 6: #match face to yellow
                    face = self.yellow
            self.rotateCW(face)