import random

class Cube:

    def __init__(self, white=['w']*9, red=['r']*9, blue=['b']*9, yellow=['y']*9, green=['g']*9, orange=['o']*9):
        self.white = white
        self.red = red
        self.blue = blue
        self.yellow = yellow
        self.green = green
        self.orange = orange
        self.movesToSolve = []

        # dictionary below not currently in use
        self.matchCharToFace = {'w': self.white, 'r': self.red, 'b': self.blue, 'y': self.yellow, 'g': self.green, 'o': self.orange}
        
        self.matchStringToFace = {'white': self.white, 'red': self.red, 'blue': self.blue, 'yellow': self.yellow, 'green': self.green, 'orange': self.orange}
        # this will be used for easily taking in a list representing a face, and then finding which face it corresponds to.
        # It seems redundant, but is necessary because hashmaps can't store lists as keys, since keys are dynamic.
        
        self.whiteFaces = {'front': self.white, 'top': self.red, 'right': self.green, 'bottom': self.orange, 'left': self.blue, 'back': self.yellow}
        self.redFaces = {'front': self.red, 'top': self.yellow, 'right': self.green, 'bottom': self.white, 'left': self.blue, 'back': self.orange}
        self.blueFaces = {'front': self.blue, 'top': self.yellow, 'right': self.red, 'bottom': self.white, 'left': self.orange, 'back': self.green}
        self.yellowFaces = {'front': self.yellow, 'top': self.orange, 'right': self.green, 'bottom': self.red, 'left': self.blue, 'back': self.white}
        self.greenFaces = {'front': self.green, 'top': self.yellow, 'right': self.orange, 'bottom': self.white, 'left': self.red, 'back': self.blue}
        self.orangeFaces = {'front': self.orange, 'top': self.yellow, 'right': self.blue, 'bottom': self.white, 'left': self.green, 'back': self.red}
        
        self.matchFaceToColor = {'w': self.whiteFaces, 'r': self.redFaces, 'b': self.blueFaces, 'y': self.yellowFaces, 'g': self.greenFaces, 'o': self.orangeFaces}

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
    
    def getOrange(self): #return orange face
        return self.orange

    def setWhite(self, face=['w']*9):
        self.white = face

    def setBlue(self, face=['b']*9):
        self.blue = face

    def setRed(self, face=['r']*9):
        self.red = face
    
    def setGreen(self, face=['g']*9):
        self.green = face
    
    def setOrange(self, face=['o']*9):
        self.orange = face
    
    def setYellow(self, face=['y']*9):
        self.yellow = face

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
            print(face[3*i:3*i+3])
        print()

    def printCube(self): #prints the full cube in a nice format
    #note that you can see what 'color' a 9x9 grid is associated to by looking at the character in the middle (index 4)
    #note that that color piece will NEVER move
    #also be aware that this is the format of the cube the program is designed around
    #in other words, each 9x9 grid, top to bottom is oriented how the program treats each face
        for i in range(3):
            temp = [' ']* 3 + self.yellow[3*i:3*i+3] + [' '] * 6
            print(temp)
        for i in range(3):
            t = 3*i
            temp = self.blue[t:t+3] + self.red[t:t+3] + self.green[t:t+3] + self.orange[t:t+3]
            print(temp)
        for i in range(3):
            temp = [' ']* 3 + self.white[3*i:3*i+3] + [' '] * 6
            print(temp)
        print()
    
    def findFace(self, face, side): # given a face (red, white, etc.) and an assiociated side (front, back), returns face occupying that side
        faceColor = face[4]
        newFace = self.matchFaceToColor[faceColor][side]
        return newFace

    def __matchColorToFace(self, color): #takes in color abbreviation like 'w' for white and spits back associated face (like 'r' becomes red)
        return self.matchStringToFace[color]

    def __matchFaceToColor(self, face):
        match face:
            case self.white:
                return 'white'
            case self.blue:
                return 'blue'
            case self.red:
                return 'red'
            case self.green:
                return 'green'
            case self.orange:
                return 'orange'
            case self.yellow:
                return 'yellow'

    def __matchFaceToSide(self, firstFace, secondFace): #takes in a first and second face, returns position of the second face relative to the first (e.g. white, red returns 'top')
        #firstFace is essentially the frontFace which secondFace is in reference to
        if firstFace == secondFace:
            return 'front'
        match firstFace:
            case self.white:
                match secondFace:
                    case self.red:
                        return 'top'
                    case self.green:
                        return 'right'
                    case self.orange:
                        return 'bottom'
                    case self.blue:
                        return 'right'
                    case self.yellow:
                        return 'back'
            case self.blue:
                match secondFace:
                    case self.yellow:
                        return 'top'
                    case self.red:
                        return 'right'
                    case self.white:
                        return 'bottom'
                    case self.orange:
                        return 'left'
                    case self.green:
                        return 'back'
            case self.red:
                match secondFace:
                    case self.yellow:
                        return 'top'
                    case self.green:
                        return 'right'
                    case self.white:
                        return 'bottom'
                    case self.blue:
                        return 'left'
                    case self.orange:
                        return 'back'
            case self.green:
                match secondFace:
                    case self.yellow:
                        return 'yellow'
                    case self.orange:
                        return 'right'
                    case self.white:
                        return 'bottom'
                    case self.red:
                        return 'right'
                    case self.blue:
                        return 'back'
            case self.orange:
                match secondFace:
                    case self.yellow:
                        return 'top'
                    case self.blue:
                        return 'right'
                    case self.white:
                        return 'bottom'
                    case self.green:
                        return 'left'
                    case self.red:
                        return 'back'
            case self.yellow:
                match secondFace:
                    case self.orange:
                        return 'top'
                    case self.green:
                        return 'right'
                    case self.red:
                        return 'bottom'
                    case self.blue:
                        return 'right'
                    case self.white:
                        return 'back'

    def __getFaceRows(self, face, row, reverse=False): #retrieves the faces top or bottom row -- used by __findOutterTriplets()
        #t for top and b for bottom
        triplet = []
        if row == 't':
            triplet = [face[0:3],face,'row','t']
        elif row == 'b':
            triplet = [face[6:],face,'row','b']

        if reverse == True:
            triplet[0][0], triplet[0][2] = triplet[0][2], triplet[0][0]
        return triplet
        
    def __getFaceCols(self, face, col, reverse=False): #retrieves the faces left or right column -- used by __findOutterTriplets()
        #l for left and r for right
        triplet = []
        if col == 'l':
            triplet = [[face[0],face[3],face[6]],face,'column','l']
        elif col == 'r':
            triplet = [[face[2],face[5],face[8]],face,'column','r']

        if reverse == True:
            triplet[0][0], triplet[0][2] = triplet[0][2], triplet[0][0]
        return triplet

    def __changeFaceRows(self, face, newRow, row): #changes the appropriate row after a rotation -- used by rotateCW()
        #t for top and b for bottom
        if row == 't':
            face[0:3] = newRow
        elif row == 'b':
            face[6:] = newRow
    
    def __changeFaceColumns(self, face, newColumn, col): #changes the appropriate column after a rotation -- used by rotateCW()
        #l for left and r for right
        if col == 'l':
            face[0] = newColumn[0]
            face[3] = newColumn[1]
            face[6] = newColumn[2]
        elif col == 'r':
            face[2] = newColumn[0]
            face[5] = newColumn[1]
            face[8] = newColumn[2]

    def __findOutterTriplets(self, frontFace): #used for side cubies that are used rotating a face -- used by rotateCW()
        """
        find the triplets on the outer edge of the face
        because the faces are described top to bottom relative to the bottom face
        the orientation of the cube means that for the program to access the triplets correctly while maintaing proper geometry,
        it needs to access them differently depending on which 'front face' we are using as a reference
        i.e. some cublets are part of a row from a different face, while others are part of a column

        This program handles it on a case by case basis, and for each of the four outter faces,
        it returns a list triplet containing the three cublets lining the front face, the face the cublets are from
        and whether they are part of a column (and if its a colun whether its the left or right one)
        or part of a row (and if its a row then whether its the left or right row) 

        NOTE: sometimes the triplets need to reversed to get an accurate rotation. When it is necessary, an extra parameter (boolean True)
        is used in the function calls.
        When to use the extra True parameter is best accepted as the result of trial and error
        """
    
        #NOTE: outter faces will always be listed in the clockwise order of
        #topFace, rightFace, bottomFace, leftFace
        if frontFace == self.white: #red, green, orange, blue
            return [self.__getFaceRows(self.red,'b'), self.__getFaceRows(self.green,'b'), self.__getFaceRows(self.orange,'b'), self.__getFaceRows(self.blue,'b')]
        elif frontFace == self.blue: #yellow, red, white, orange
            return [self.__getFaceCols(self.yellow,'l'), self.__getFaceCols(self.red,'l'), self.__getFaceCols(self.white,'l',True), self.__getFaceCols(self.orange,'r',True)]
        elif frontFace == self.red: #yellow, green, white, blue
            return [self.__getFaceRows(self.yellow,'b'), self.__getFaceCols(self.green,'l',True), self.__getFaceRows(self.white,'t'), self.__getFaceCols(self.blue,'r',True)]
        elif frontFace == self.green: #yellow, orange, white, red
            return [self.__getFaceCols(self.yellow,'r',True), self.__getFaceCols(self.orange,'l',True), self.__getFaceCols(self.white,'r'), self.__getFaceCols(self.red,'r')]
        elif frontFace == self.yellow: #orange, green, red, blue
            return [self.__getFaceRows(self.orange,'t'), self.__getFaceRows(self.green,'t'), self.__getFaceRows(self.red,'t')   ,self.__getFaceRows(self.blue,'t')]
        elif frontFace == self.orange: #yellow, blue, white, green
            return [self.__getFaceRows(self.yellow,'t',True), self.__getFaceCols(self.blue,'l'), self.__getFaceRows(self.white,'b',True), self.__getFaceCols(self.green,'r')]

    def rotateCW(self, frontFace, trackMoves = True): # master function used for all rotations
        #trackMoves says whether or not to add the rotations to the cube

        if trackMoves:
            self.movesToSolve.append(self.__matchFaceToColor(frontFace))

        triplets = self.__findOutterTriplets(frontFace)
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

            #for __changeFaceRows and __changeFaceColumns, input is: i) face being updated, ii) the new triplet, and iii) the row/column being updated
            if isRowOrCol == 'row':
                self.__changeFaceRows(tripletFace,newTriplet,triplets[i][-1])
            else:
                self.__changeFaceColumns(tripletFace,newTriplet,triplets[i][-1])
           
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
            self.rotateCW(face, False)
            #since scrambleCube() is mostly used for testing, we set it to ignore the changes it makes to the cube

    def __simplifySolution(self): #takes the array containg the solution moves and makes it human-readable
        try:
            newSolutionMoves = []
            for i in range(len(self.movesToSolve)):
                if i > 0 and self.movesToSolve[i] == self.movesToSolve[i-1]:
                    newSolutionMoves[-1][1] += 1
                else:
                    newSolutionMoves.append([self.movesToSolve[i], 1])
            self.movesToSolve[:] = newSolutionMoves
            newSolutionMoves = []

            for i in range(len(self.movesToSolve)):
                self.movesToSolve[i][1] %= 4
                if self.movesToSolve[i][1] != 0:
                    newSolutionMoves.append(self.movesToSolve[i])
                else:
                    continue
            self.movesToSolve[:] = newSolutionMoves
            newSolutionMoves = []

            def convertNumRotationsToStr(numRotations):
                match numRotations:
                    case 1:
                        return ' CW once'
                    case 2:
                        return ' CW twice'
                    case 3:
                        return ' CCW once'

            for i in range(len(self.movesToSolve)):
                s = self.__matchFaceToSide(self.white, self.__matchColorToFace(self.movesToSolve[i][0])) + convertNumRotationsToStr(self.movesToSolve[i][1])
                newSolutionMoves.append(s)
            self.movesToSolve[:] = newSolutionMoves
        except:
            pass

    def printMovesToSolve(self): #prints the moves to solve the cube
        self.__simplifySolution()
        for i in range(0, len(self.movesToSolve), 10):
            print(self.movesToSolve[i:i+10])
            print()
        print(len(self.movesToSolve))