from Cube import Cube

class RegularAlgorithms(Cube):

    """
    NOTE:
    USEFUL REFERENCE FOR GETTING THE GENERIC ALGORITHMS 
    https://rubiks-cube-solver.com/how-to-solve/
    """

    def __init__(self, white=['w']*9, red=['r']*9, blue=['b']*9, yellow=['y']*9, green=['g']*9, orange=['o']*9):
        super().__init__(white, red, blue, yellow, green, orange)
    
    # solving the white layer

    def getWhiteCross(self): #gets white cross without regard for proper edge alignment

        def alignSideEdges(frontFace, topFace, leftFace, whiteEdgeIndex): #aligns white edges that are on non-yellow and non-white faces
            #whiteEdgeIndex ensures that we do no move a white edge into a position where there is already a white edge
            #thus defeating the purpose
            if frontFace[1] == 'w' or frontFace[3] == 'w' or frontFace[5] == 'w' or frontFace[7] == 'w':
                while self.white[whiteEdgeIndex] == 'w':
                    self.rotateCW(self.white)
                while frontFace[7] != 'w':
                    self.rotateCW(frontFace)
                self.rotateCW(frontFace)
                self.rotateCCW(leftFace)
                self.rotateCCW(topFace)
                self.rotateCW(leftFace)
                self.rotateCW(frontFace)
                self.rotateCW(frontFace)

        def alignYellowEdges(frontFace, whiteEdgeIndex, yellowEdgeIndex): #aligns white edges that are on the yellow face
            #whiteEdgeIndex serves same purpose as in alignSideEdges()
            # the idea is that if there is a white edge on the yellow face,
            # we want to move it up to the white face by rotating an appropriate face twice
            # however, if that can unintentionally move a white edge down to yellow in the process, creating an infinite loop
            # therefore, we always check if the edge on the white face opposing the edge on the yellow face is white first, and move it if it is!
            if self.yellow[yellowEdgeIndex] == 'w':
                while self.white[whiteEdgeIndex] == 'w':
                    self.rotateCW(self.white)
                self.rotateCW(frontFace)
                self.rotateCW(frontFace)

        while self.white[1] != 'w' or self.white[3] != 'w' or self.white[5] != 'w' or self.white[7] != 'w':
        #in testing, loop has never had to be run more than 3 times
        # first section: moving all white edges on the yellow face up to the white face 
            face = self.findFace(self.yellow, 'top')
            whiteEdgeIndex = 7
            yellowEdgeIndex = 1
            alignYellowEdges(face, whiteEdgeIndex, yellowEdgeIndex)

            face = self.findFace(self.yellow, 'right')
            whiteEdgeIndex = 5
            yellowEdgeIndex = 5
            alignYellowEdges(face, whiteEdgeIndex, yellowEdgeIndex)

            face = self.findFace(self.yellow, 'bottom')
            whiteEdgeIndex = 1
            yellowEdgeIndex = 7
            alignYellowEdges(face, whiteEdgeIndex, yellowEdgeIndex)

            face = self.findFace(self.yellow, 'left')
            whiteEdgeIndex = 3
            yellowEdgeIndex = 3
            alignYellowEdges(face, whiteEdgeIndex, yellowEdgeIndex)

        #second section: moving all white edges on the faces surrounding white up to the white face
            face = self.findFace(self.white, 'top') #red
            whiteEdgeIndex = 1
            topFace = self.yellow #top face will always be yellow in this function, so it doesn't need to be changed later
            leftFace = self.findFace(face, 'left')
            alignSideEdges(face, topFace, leftFace, whiteEdgeIndex)

            face = self.findFace(self.white, 'right') #green
            leftFace = self.findFace(face, 'left')
            whiteEdgeIndex = 5
            alignSideEdges(face, topFace, leftFace, whiteEdgeIndex)

            face = self.findFace(self.white, 'bottom') #orange
            leftFace = self.findFace(face, 'left')
            whiteEdgeIndex = 7
            alignSideEdges(face, topFace, leftFace, whiteEdgeIndex)

            face = self.findFace(self.white, 'left') #blue
            leftFace = self.findFace(face, 'left')
            whiteEdgeIndex = 3
            alignSideEdges(face, topFace, leftFace, whiteEdgeIndex)

    def swapNeighboringWhiteEdges(self, firstFace, secondFace): #swaps adjacent edges -- used by alignWhite()
        """
        If you have two edges which are next to each other (rather than opposite, which is handled in swapOppositeWhiteEdges())
        this function will swap them.
        The idea for this function is as follows:
            - Of the two edges that need to be swapped, take the one on the right (could also use left, but this will always use right for simplicity)
            - So take the face of the right-hand edge, rotate it twice so that its on the bottom of the cube (on the yellow face)
            - Rotate that face (in this case the bottom/yellow face) counter-clockwise once so that it is now opposite the other edge it is swapping
            - Rotate the left face twice so that what was previously the right-edge has now replaced the left-edge on top, and the left-edge is now
            on the bottom of the cube
            - rotate the bottom face (yellow in this case) clockwise once
            - rotate the right face twice to put what was previously the left-edge on top to where the right-edge used to be

        Implementations of this algorithm will depend on the edges being swapped
        """
        topFace = self.yellow #the top face will always be yellow in this function

        self.rotateCW(firstFace)
        self.rotateCW(firstFace)
        self.rotateCCW(topFace)
        self.rotateCW(secondFace)
        self.rotateCW(secondFace)
        self.rotateCW(topFace)
        self.rotateCW(firstFace)
        self.rotateCW(firstFace) 

    def swapOppositeWhiteEdges(self, firstFace, secondFace): # swaps opposite edges -- used by alignWhite()
        """
        Used to swap edges on the opposite sides of the white face
        It first moves the middle row/column that has the edges which need to be swapped to the opposite side of the cube
        It then rotates that row/column 180 degrees so that the edges are now on opposite sides of the cube 
        and then moves the row/column back to the middle of the white face
g
        NOTE: this move is physically equivalent to rotating the middle row/column twice, then rotating that face twice,
        then rotating that middle row/column two more itmes to be back in line with the white face.
        """
        self.rotateCW(firstFace)
        self.rotateCW(firstFace)
        self.rotateCW(secondFace)
        self.rotateCW(secondFace)
        self.rotateCW(self.white)
        self.rotateCW(self.white)
        self.rotateCW(firstFace)
        self.rotateCW(firstFace)
        self.rotateCW(secondFace)
        self.rotateCW(secondFace)

    def alignWhite(self): #gets proper edge alignment once white cross is in place -- used by solveWhiteLayer()
        
        while self.red[7] != 'r': #using the red face as a baseline
            self.rotateCW(self.white)
        
        if self.green[7] != 'g': #going around the cube clockwise, checking edges
            if self.orange[7] == 'g':
                self.swapNeighboringWhiteEdges(self.green, self.orange)
            else:
                self.swapOppositeWhiteEdges(self.red, self.orange)
        
        if self.orange[7] != 'o': #no need to check the blue edge at this point
            self.swapNeighboringWhiteEdges(self.orange, self.blue)
        
    def solveFrontFacingCorner(self, face): #solves corners facing forwards, or on the right side of a face -- used by solveWhiteCorners()
        topFace = self.findFace(face, 'top')
        leftFace = self.findFace(face, 'left')

        self.rotateCCW(topFace)
        self.rotateCCW(leftFace)
        self.rotateCW(topFace)
        self.rotateCW(leftFace)

    def solveSideFacingCorner(self, face): #solves corners facing sidewayas, or on the left side of a face -- used by solveWhiteCorners()
        topFace = self.findFace(face, 'top') #returns self.yellow (assuming face=self.red by default)
        leftFace = self.findFace(face, 'left') #returns self.blue (assuming face=self.red by default)
        
        self.rotateCCW(leftFace)
        self.rotateCCW(topFace)
        self.rotateCW(leftFace)

    def solveBottomFacingCorner(self, face): #solves corners facing the bottom (meaning that part of the yellow face is white) -- used by solveWhiteCorners()
        leftFace = self.findFace(face, 'left') #returns self.blue (assuming face=self.red by default)
        topFace = self.findFace(face, 'top') #returns self.yellow (assuming face=self.red by default)
        
        self.rotateCCW(leftFace)
        self.rotateCW(topFace)
        self.rotateCW(topFace)
        self.rotateCW(leftFace)
        self.rotateCW(topFace)
        self.rotateCCW(leftFace)
        self.rotateCCW(topFace)
        self.rotateCW(leftFace)

    def findWhiteCornersUPPER(self, leftCornerColor, rightCornerColor): #look in the cube for a specific white corner
        face = self.findFace(self.white, 'back') #this returns self.yellow
        leftFace = self.findFace(face, 'left') #this returns self.blue
        bottomFace = self.findFace(face, 'bottom')

        """
        Since white corners cannot be found on edges, if follows that they can only be found on the top or bottom layer of a cube
        In this case, that means that each white corner exists in some **any** orientation on the white face (bottom) or yellow face (upper)
        The 'UPPER' in the function name is because this function checks the yellow face for white corners, and I could not think of a better name

        The white-part of a white corner in top/upper layer may not be in the top layer itself. For example, the white part could be in the blue face
        while the yellow face contains the blue part, etc. The function checks for each of the three possible arrangements

        To reduce the number of places to check, this function rotates the top layer up to 4 times, each time checking if the corner at [7] is 
        a white corner.
        If the corner is a white corner, it figures out whether it is a frontFacingCorner, sideFacingCorner, or bottomFacingCorner,
        returning 'front', 'side' and 'bottom' respectively.
        """

        numChecks = 1
        while numChecks <= 4: #after 4 checks/rotations, we know that we have checked every corner of the yellow face
            if face[6]==rightCornerColor and leftFace[2]==leftCornerColor and bottomFace[0]=='w':
                return 'front'
            elif face[6]==leftCornerColor and leftFace[2]=='w' and bottomFace[0]==rightCornerColor:
                return 'side'
            elif face[6]=='w' and leftFace[2]==rightCornerColor and bottomFace[0]==leftCornerColor:
                return 'bottom'
            else:
                self.rotateCW(face)
                numChecks += 1
            #NOTE: THERE ARE TECHNICALLY OTHER WAYS THE CORNERS COULD BE ARRANGED, BUT THE OTHER ARRANGEMENTS ARE ONLY POSSIBLE IF 
            # THE CORNERS HAVE BEEN FLIPPED
            # In the future, that could be a good way to tell the users whether or not their cube has been tampered with/has flipped corners
            # and possibly tell them how to flip the corners back

        return 'x' #for debugging, incase it doesn't find any corners    
    
    def findWhiteCornersLOWER(self, leftCornerColor, rightCornerColor): #search bottom of cube for specific white corner, move to top layer if found
        face = self.white
        leftFace = self.findFace(face, 'left') #returns self.blue
        topFace = self.findFace(face, 'top') #returns self.red
        backFace = self.findFace(face, 'back') #returns self.yellow, only used in moveCorner()
        """
        This function only checks if there is a misplaced white corner in the lower layer (which is self.white)
        and doesn't provide any more information beyond that. The reason is because to solve a white corner in the lower layer,
        the corner gets moved to the upper layer. 
        Therefore, this program just checks if a white corner is in the upper layer and if it is, moves it to the upper layer
        and then letters findWhiteCornersUPPER() handle the rest.
        As a consequence, this function also does not check whether a corner arrangement is valid (like if a corner has been flipped)
        like findWhiteCornersUPPER() does, since that will be handled later.
        """
        def moveCorner(): #perform to move white corners to the top layer
            self.rotateCCW(leftFace)
            self.rotateCW(backFace)
            self.rotateCW(backFace)
            self.rotateCW(leftFace)

        numChecks = 1
        while numChecks <= 4:
            if face[0]=='w' and leftFace==leftCornerColor and topFace==rightCornerColor:
                break #skip this case because in this case the corner is oriented correctly
                #this case presumably does not happen because if a corner is oriented correctly,
                #identifyWhiteCorners() and/or solveWhiteCorners() should not call this function
                #this case is added as a backup
            elif face[0]=='w' and leftFace[8]==rightCornerColor and topFace[6]==leftCornerColor:
                moveCorner()
                break
            elif face[0]==leftCornerColor and leftFace[8]=='w' and topFace[6]==rightCornerColor:
                moveCorner()
                break
            elif face[0]==leftCornerColor and leftFace[8]==rightCornerColor and topFace[6]=='w':
                moveCorner()
                break
            elif face[0]==rightCornerColor and leftFace[8]=='w' and topFace[6]==leftCornerColor:
                moveCorner()
                break
            elif face[0]==rightCornerColor and leftFace[8]==leftCornerColor and topFace[6]=='w':
                moveCorner()
                break
            else:
                numChecks += 1
                self.rotateCW(face)
            
        while numChecks <= 4: #this step is necessary to return the white face of the cube to its original state when this function was called
            #otherwise the white edges will not line up with the desired leftCorner and rightCorner
            self.rotateCW(face)
            numChecks += 1

    def solveWhiteCorners(self): #solves the white corners
        face = self.white
        leftFace = self.findFace(face, 'left') #returns self.blue
        rightFace = self.findFace(face, 'top') #returns self.red

        frontFace = self.red #all operations solving the white corners will be done by considering the red face as the default front

        """
        Every corner has three sides and three colors. Here, we know that we want white[0] to be white, and leftCornerColor
        and rightCornerColor tell us what the other two colors will be (geometrically, rightCornerColor will be on the 'top', but we still refer
        to it as 'rightCornerColor')
        
        To reduce the complexity of gauging whether each corner is in the correct place, and finding the locations of finding
        relevant corners throughout the cube, the program will ***always rotate the faces in such a way that the necessary corner pieces can be 
        looked for in the same place***.
        That is, a corner on the white face that needs to be solved will always be rotated so it is at white[0], so that we can always check the
        corners other colors by looking in self.blue and self.red
        """

        while self.white != ['w'] * 9:
            leftCornerColor = leftFace[7] #returns self.blue[7]
            rightCornerColor = rightFace[7] #returns self.red[7]

            cornerUnsolved = False
            cornerLocation = ""

            #checking if the corner colors matches the edge color
            if leftCornerColor != leftFace[8] or rightCornerColor != rightFace[6] or face[0] != 'w':
                cornerUnsolved = True
            
            if cornerUnsolved:
                self.findWhiteCornersLOWER(leftCornerColor, rightCornerColor)
                cornerLocation = self.findWhiteCornersUPPER(leftCornerColor, rightCornerColor)
                if cornerLocation == 'front':
                    self.solveFrontFacingCorner(frontFace)
                elif cornerLocation == 'side':
                    self.solveSideFacingCorner(frontFace)
                elif cornerLocation == 'bottom':
                    self.solveBottomFacingCorner(frontFace)
            
            self.rotateCW(face) #rotates self.white CW since face = self.white

    def solveWhiteLayer(self): #master function for solving the white layer
        self.getWhiteCross()
        self.alignWhite()
        self.solveWhiteCorners()
        self.alignWhite() #after solveWhiteCorners, this will really only rotate the cube until the edge colors match the center colors
        #of the faces surrounding self.white

    # solving the middle layer
             
    def moveEdgeToMiddleRight(self, face): #move edge on the top (along yellow face) to the middle layer on the RIGHT
        topFace = self.findFace(face, 'top')
        rightFace = self.findFace(face, 'right')

        self.rotateCW(topFace)
        self.rotateCW(rightFace)
        self.rotateCCW(topFace)
        self.rotateCCW(rightFace)
        self.rotateCCW(topFace)
        self.rotateCCW(face)
        self.rotateCW(topFace)
        self.rotateCW(face)

    def moveEdgeToMiddleLeft(self, face): #move edge on the top (along yellow face) to the middle layer on the LEFT
        topFace = self.findFace(face, 'top')
        leftFace = self.findFace(face, 'left')

        self.rotateCCW(topFace)
        self.rotateCCW(leftFace)
        self.rotateCW(topFace)
        self.rotateCW(leftFace)
        self.rotateCW(topFace)
        self.rotateCW(face)
        self.rotateCCW(topFace)
        self.rotateCCW(face)

    def solveFaceMiddleLayer(self, frontFace): #solves the middle layer of a single face -- used by solveMiddleLayer()
        leftFace = self.findFace(frontFace, 'left')
        topFace = self.findFace(frontFace, 'top') #everytime solveFaceMiddleLayer() is called, this should just return self.yellow
        rightFace = self.findFace(frontFace, 'right')
        bottomFace = self.findFace(frontFace, 'bottom') #this should return self.white everytime
        # NOTE: I am not yet sure if bottomFace will ever need to be used

        frontFaceColor = frontFace[4]

        leftEdgeColor = leftFace[4] #what colors the right and left edges **should** be
        rightEdgeColor = rightFace[4]

        leftEdgeCurrentColor = leftFace[5] #what colors the right and left edges actually are
        rightEdgecurrentColor = rightFace[3]

        frontFaceLeftColor = frontFace[3]
        frontFaceRightColor = frontFace[5]

        if leftEdgeCurrentColor != leftEdgeColor or frontFaceLeftColor != frontFaceColor:
            if leftEdgeCurrentColor == frontFaceColor: #the edge piece is in the right place but it is reversed
                self.moveEdgeToMiddleLeft(frontFace)
                self.rotateCW(topFace)
                self.rotateCW(topFace)
                self.moveEdgeToMiddleLeft(frontFace)
            else:
                numRotations = 1
                while topFace[7] != leftEdgeColor and frontFace[1] != frontFaceColor and numRotations <= 4:
                    self.rotateCW(topFace)
                    numRotations += 1
                if numRotations < 4:
                    self.moveEdgeToMiddleLeft(frontFace)
            
        if rightEdgecurrentColor != rightEdgeColor or frontFaceRightColor != frontFaceColor:
            if rightEdgecurrentColor == frontFaceColor: #the edge piece is in the right place but it is reversed
                self.moveEdgeToMiddleRight(frontFace)
                self.rotateCW(topFace)
                self.rotateCW(topFace)
                self.moveEdgeToMiddleRight(frontFace)
            else:
                numRotations = 1
                while topFace[7] != rightEdgeColor and frontFace[1] != frontFaceColor and numRotations <= 4:
                    self.rotateCW(topFace)
                    numRotations += 1
                if numRotations < 4:
                    self.moveEdgeToMiddleRight(frontFace)
            
    def solveMiddleLayer(self): #master function that solves the middle layer of the whole cube

        def middleLayerSolved(): #check if the middle layer is solved
            if self.red[3:6] != ['r']*3 or self.green[3:6] != ['g']*3 or self.orange[3:6] != ['o']*3 or self.blue[3:6] != ['b']*3:
                return False
            else:
                return True
            
        while not middleLayerSolved():
            self.solveFaceMiddleLayer(self.red)
            self.solveFaceMiddleLayer(self.green)
            self.solveFaceMiddleLayer(self.orange)
            self.solveFaceMiddleLayer(self.blue)

            #if the self.solveFaceMiddleLayer(face) is not staggered,
            #it can cause an infinite loop because one face can depend on a later face being solved
            #the if-else statements to prevent the looop from going on longer than it needs to

            if not middleLayerSolved():
                self.solveFaceMiddleLayer(self.green)
                self.solveFaceMiddleLayer(self.orange)
                self.solveFaceMiddleLayer(self.blue)
                self.solveFaceMiddleLayer(self.red)
            else:
                break

            if not middleLayerSolved():
                self.solveFaceMiddleLayer(self.orange)
                self.solveFaceMiddleLayer(self.blue)
                self.solveFaceMiddleLayer(self.red)
                self.solveFaceMiddleLayer(self.green)
            else:
                break

            if not middleLayerSolved():
                self.solveFaceMiddleLayer(self.blue)
                self.solveFaceMiddleLayer(self.red)
                self.solveFaceMiddleLayer(self.green)
                self.solveFaceMiddleLayer(self.orange)
            else:
                break

    # getting the final layer

    def doYellowLineAlgorithm(self, frontFace): #algorithm for when theres a line or a dot on the yellow face
        #note that frontFace could actually vary, and should never be self.yellow
        topFace = self.findFace(frontFace, 'top') #this should always return self.yellow
        rightFace = self.findFace(frontFace, 'right')

        self.rotateCW(frontFace)
        self.rotateCW(rightFace)
        self.rotateCW(topFace)
        self.rotateCCW(rightFace)
        self.rotateCCW(topFace)
        self.rotateCCW(frontFace)
    
    def doYellowLAlgorithm(self, frontFace): #the algorithm for when there is an 'L' shape on the yellow face
        topFace = self.findFace(frontFace, 'top')
        rightFace = self.findFace(frontFace, 'right')

        self.rotateCW(frontFace)
        self.rotateCW(topFace)
        self.rotateCW(rightFace)
        self.rotateCCW(topFace)
        self.rotateCCW(rightFace)
        self.rotateCCW(frontFace)

    def solveYellowCross(self): #gets the yellow cross
        face = self.red
        topFace = self.findFace(face, 'top') #this will always return yellow when face = self.red

        def getNumEdges(): #counts the number of yellow edges
            numEdges = 0
            if topFace[1]=='y':
                numEdges +=1
            if topFace[3]=='y':
                numEdges +=1
            if topFace[5]=='y':
                numEdges +=1
            if topFace[7]=='y':
                numEdges +=1
            return numEdges

        while getNumEdges() != 4:
            while topFace[7] == 'y':
                self.rotateCW(topFace)

            if getNumEdges() == 0:
                self.doYellowLineAlgorithm(face)
            elif getNumEdges() == 2:
                if topFace[3] == 'y' and topFace[5] == 'y': #topFace[1]==topFace[7]=='y' prevented by nested while loop
                    self.doYellowLineAlgorithm(face)
                else:
                    while topFace[1] != 'y' or topFace[3] != 'y':
                        self.rotateCW(topFace)
                    self.doYellowLAlgorithm(face)

    def swapAdjacentYellowEdges(self, frontFace): #swaps a yellow edge with the next yellow edge going clockwise
        #note that frontFace should never be yellow
        topFace = self.findFace(frontFace, 'top') #should always return yellow
        rightFace = self.findFace(frontFace, 'right')

        self.rotateCW(rightFace)
        self.rotateCW(topFace)
        self.rotateCCW(rightFace)
        self.rotateCW(topFace)
        self.rotateCW(rightFace)
        self.rotateCW(topFace)
        self.rotateCW(topFace)
        self.rotateCCW(rightFace)
        self.rotateCW(topFace)

    def alignYellowCross(self): #aligns edge pieces of yellow cross. Note it uses a different algorithm from aligning the white cross
        topFace = self.yellow
        face = self.red

        def crossAligned(): #check if the cross is aligned
            while self.red[1] != 'r':
                self.rotateCW(topFace)
            if self.red[1]=='r' and self.green[1]=='g' and self.orange[1]=='o' and self.blue[1]=='b':
                return True
            else:
                return False

        while not crossAligned(): #note that crossAligned() will always rotate the yellow face
            #until the bottom edge matches the red face, so that part of the cube will always be aligned when we go through this loop
            #That is important because the code in this loop is structure around the assumption red[1]=='r'
            
            if self.blue[1] != 'b':
                self.swapAdjacentYellowEdges(self.blue)
            
            if self.orange[1] != 'o':
                self.swapAdjacentYellowEdges(self.orange)

            #here we are just swapping blue[1] with orange[1] and (if necessary) orange[1] and green[1] 
            #until things work out
    
    def moveYellowCorner(self, frontFace): #algorithm for moving yellow corners into place
        rightFace = self.findFace(frontFace, 'right')
        bottomFace = self.findFace(frontFace, 'bottom')

        self.rotateCCW(rightFace)
        self.rotateCCW(bottomFace)
        self.rotateCW(rightFace)
        self.rotateCW(bottomFace)

    def positionYellowCorners(self, frontFace):
        topFace = self.findFace(frontFace, 'top')
        rightFace = self.findFace(frontFace, 'right')
        leftFace = self.findFace(frontFace, 'left')

        self.rotateCW(topFace)
        self.rotateCW(rightFace)
        self.rotateCCW(topFace)
        self.rotateCCW(leftFace)
        self.rotateCW(topFace)
        self.rotateCCW(rightFace)
        self.rotateCCW(topFace)
        self.rotateCW(leftFace)

    def moveYellowCorner(self, frontFace):
        rightFace = self.findFace(frontFace, 'right')
        bottomFace = self.findFace(frontFace, 'bottom')

        self.rotateCCW(rightFace)
        self.rotateCCW(bottomFace)
        self.rotateCW(rightFace)
        self.rotateCW(bottomFace)

    def solveYellowCorners(self): #gets the yellow corners into place, completing the cube
        frontFace = self.red
        leftFace = self.findFace(frontFace, 'left') #returns self.blue
        topFace = self.findFace(frontFace, 'top') #returns self.yellow
        rightFace = self.findFace(frontFace, 'right') #returns self.green

        def checkIfGoodCorner(): # a good corner is a yellow corner that is placed correctly (roughly speaking)
            #the if statements show the conditions to be a good corner
            if rightFace[0]=='y' and frontFace[2]==rightFace[1] and topFace[8]==frontFace[1]:
                return True
            elif frontFace[2]=='y' and rightFace[0]==frontFace[1] and topFace[8]==rightFace[1]:
                return True
            elif topFace[8]=='y' and frontFace[2]==frontFace[1] and rightFace[0]==rightFace[1]:
                return True
            else:
                return False

        def findGoodCorner():
            for i in range(4):
                if checkIfGoodCorner():
                    break
                else:
                    self.rotateCW(topFace)
        
        def getNumGoodCorners():
            numGoodCorners = 0
            for i in range(4):
                if checkIfGoodCorner():
                    numGoodCorners += 1
                self.rotateCW(topFace)
            return numGoodCorners
        
        def moveCorner(): #moves a 'good' corner to be in the top right of front face
            while frontFace[2] != 'y':
                self.rotateCW(topFace)

        if getNumGoodCorners() == 0:
            self.positionYellowCorners(frontFace)
        
        findGoodCorner()
        if getNumGoodCorners != 4:
            self.positionYellowCorners(frontFace)
        findGoodCorner()
        if getNumGoodCorners != 4:
            self.positionYellowCorners(frontFace)

        cube.printCube()

        while topFace != ['y']*9:
            moveCorner()
            self.moveYellowCorner(frontFace)




        cube.printCube()

    def solveCube(self): #master function to solve the cube
        self.solveWhiteLayer()
        self.solveMiddleLayer()
        self.solveYellowCross()
        self.alignYellowCross()

cube = RegularAlgorithms()

cube.scrambleCube(5000)


cube.scrambleCube(100)
cube.solveCube()
cube.printCube()

cube.solveYellowCorners()
cube.printCube()

cube.userOperation()