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
            if self.orange == 'g':
                self.swapNeighboringWhiteEdges(self.green, self.orange)
            else:
                self.swapOppositeWhiteEdges(self.red, self.orange)

        if self.orange[7] != 'o': #no need to check the blue edge at this point
            self.swapNeighboringWhiteEdges(self.orange, self.blue)
        
    def solveFrontFacingCorner(self, face): #solves corners facing forwards, or on the right side of a face -- used by solveWhiteCorners()
        topFace = self
        topFace = self.findFace(face, 'top')
        leftFace = self.findFace(face, 'left')

        self.rotateCCW(topFace)
        self.rotateCCW(leftFace)
        self.rotateCW(topFace)
        self.rotateCW(leftFace)

    def solveSideFacingCorner(self, face): #solves corners facing sidewayas, or on the left side of a face -- used by solveWhiteCorners()
        topFace = self.findFace(face, 'top')
        leftFace = self.findFace(face, 'left')
        
        self.rotateCCW(leftFace)
        self.rotateCCW(topFace)
        self.rotateCW(leftFace)

    def solveWhiteCorners(self): # master function for solving the white corners -- used by solveWhiteLayer()
        # FIXME: ADD FUNCTIONALITY
        pass

    def solveWhiteLayer(self): # master function for solving the white layer
        self.getWhiteCross()
        self.alignWhite()
        self.solveWhiteCorners()
        self.alignWhite() # NOTE: this last call might not be necessary, depending on how solveWhiteCorners() ends up being coded

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

    def alignMiddleEdges(self): #aligns the middle edges
        pass