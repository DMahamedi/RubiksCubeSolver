from Cube import Cube

class RegularAlgorithms(Cube):

    """
    NOTE:
    USEFUL REFERENCE FOR GETTING THE GENERIC ALGORITHMS 
    https://rubiks-cube-solver.com/how-to-solve/
    """

    def __init__(self, white=['w']*9, red=['r']*9, blue=['b']*9, yellow=['y']*9, green=['g']*9, orange=['o']*9):
        super().__init__(white, red, blue, yellow, green, orange)
    
    def getWhiteCross(self):
        # the white cross is created without regard for the proper alignment of the edge pieces to the center pieces
        # alignment to the center pieces is handled seperately

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
        # first section: moving all white edges on the yellow face up to the white face 
            face = self.findFrontFace(self.yellow, 'top')
            whiteEdgeIndex = 7
            yellowEdgeIndex = 1
            alignYellowEdges(face, whiteEdgeIndex, yellowEdgeIndex)

            face = self.findFrontFace(self.yellow, 'right')
            whiteEdgeIndex = 5
            yellowEdgeIndex = 5
            alignYellowEdges(face, whiteEdgeIndex, yellowEdgeIndex)

            face = self.findFrontFace(self.yellow, 'bottom')
            whiteEdgeIndex = 1
            yellowEdgeIndex = 7
            alignYellowEdges(face, whiteEdgeIndex, yellowEdgeIndex)

            face = self.findFrontFace(self.yellow, 'left')
            whiteEdgeIndex = 3
            yellowEdgeIndex = 3
            alignYellowEdges(face, whiteEdgeIndex, yellowEdgeIndex)
        #that concludes removing the white edges from yellow

        #second section: moving all white edges on the faces surrounding white up to the white face
            face = self.findFrontFace(self.white, 'top') #red
            whiteEdgeIndex = 1
            topFace = self.yellow #top face will always be yellow in this function, so it doesn't need to be changed later
            leftFace = self.findFrontFace(face, 'left')
            alignSideEdges(face, topFace, leftFace, whiteEdgeIndex)

            face = self.findFrontFace(self.white, 'right') #green
            leftFace = self.findFrontFace(face, 'left')
            whiteEdgeIndex = 5
            alignSideEdges(face, topFace, leftFace, whiteEdgeIndex)

            face = self.findFrontFace(self.white, 'bottom') #orange
            leftFace = self.findFrontFace(face, 'left')
            whiteEdgeIndex = 7
            alignSideEdges(face, topFace, leftFace, whiteEdgeIndex)

            face = self.findFrontFace(self.white, 'left') #blue
            leftFace = self.findFrontFace(face, 'left')
            whiteEdgeIndex = 3
            alignSideEdges(face, topFace, leftFace, whiteEdgeIndex)

        #end of second section

    def swapNeighboringWhiteEdges(self, firstEdge, secondEdge): # FIXME: ADD FUNCTIONALITY
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

    def swapOppositeWhiteEdges(self, firstEdge, secondEdge):
        """
        Used to swap edges on the opposite sides of the white face
        It first moves the middle row/column that has the edges which need to be swapped to the opposite side of the cube
        It then rotates that row/column 180 degrees so that the edges are now on opposite sides of the cube 
        and then moves the row/column back to the middle of the white face

        NOTE: this move is physically equivalent to rotating the middle row/column twice, then rotating that face twice,
        then rotating that middle row/column two more itmes to be back in line with the white face.
        """
        def swapOperation(firstFace, secondFace):
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

        if firstEdge==1 and secondEdge==7:
            leftFace = self.findFrontFace(self.white, 'left')
            rightFace = self.findFrontFace(self.white, 'right')
            swapOperation(leftFace, rightFace)

        elif firstEdge==3 and secondEdge==5:
            topFace = self.findFrontFace(self.white, 'top')
            bottomFace = self.findFrontFace(self.white, 'bottom')
            swapOperation(topFace, bottomFace)

        else:
            print("error in swapOpppositeWhiteEdges()")

    def alignWhite(self): #gets proper edge alignment once white cross is in place
        firstEdge = self.matchColorToFace(self.white[1])
        

cube = RegularAlgorithms()

cube.scrambleCube(500)

cube.printCube()

print()

cube.getWhiteCross()

cube.printCube()

cube.userOperation()