from Cube import Cube

class RegularAlgorithms(Cube):

    """
    NOTE:
    USEFUL REFERENCE FOR GETTING THE GENERIC ALGORITHMS 
    https://rubiks-cube-solver.com/how-to-solve/
    """

    def __init__(self, white=['w']*9, red=['r']*9, blue=['b']*9, yellow=['y']*9, green=['g']*9, orange=['o']*9):
        super().__init__(white, red, blue, yellow, green, orange)
    
    def checkEdgePieces(self, face, color):
        colorToChar = {'white': 'w', 'blue': 'b', 'red':'r', 'green':'g', 'orange':'o', 'yellow':'y'}
        colorChar = colorToChar[color]
        edgePieceIndex = -1 #-1 default incase edge piece not found
        if face[1] == colorChar:
            edgePieceIndex = 1
        elif face[3] == colorChar:
            edgePieceIndex = 3
        elif face[5] == colorChar:
            edgePieceIndex = 5
        elif face[7] == colorChar:
            edgePieceIndex = 7
        return edgePieceIndex
    
    def moveEdgePieces(self, face, edgePieceIndex): #NOTE: FOR THE TIME BEING, THIS WILL BE USED TO MOVE WHITE EDGE PIECES
        nextFace = face
        if face != self.yellow: #because yellow is in a weird place relative to white
            if edgePieceIndex == 1:
                self.rotateCW(face)
                nextFace = self.findFrontFace(face,'right')
                self.rotateCCW(nextFace)
            elif edgePieceIndex == 3:
                nextFace = self.findFrontFace(face,'left')
                self.rotateCW(nextFace)
            elif edgePieceIndex == 5:
                nextFace = self.findFrontFace(face,'right')
                self.rotateCCW(nextFace)
            elif edgePieceIndex == 7: #FIXME: CHECK THAT THIS ACTUALLY WORKS FOR edgePieceIndex==7
                nextFace = self.findFrontFace(face, 'bottom')
                self.rotateCW(nextFace)
        else:
            if edgePieceIndex == 1:
                nextFace = self.findFrontFace(face,'top')
            elif edgePieceIndex == 3:
                nextFace = self.findFrontFace(face, 'left')
            elif edgePieceIndex == 5:
                nextFace = self.findFrontFace(face, 'right')
            elif edgePieceIndex == 7:
                nextFace = self.findFrontFace(face, 'bottom')
            self.rotateCW(nextFace)
            self.rotateCW(nextFace)
    
    def getWhiteCross(self): #gets white cross, disregards proper edge alignment
        temp = 0 #for debugging
        while self.white[1] != 'w' or self.white[3] != 'w' or self.white[5] != 'w' or self.white[7] != 'w':
            edgePieceIndex = self.checkEdgePieces(self.red, 'white')
            if edgePieceIndex != -1:
                self.moveEdgePieces(self.red, edgePieceIndex)

            edgePieceIndex = self.checkEdgePieces(self.green, 'white')
            if edgePieceIndex != -1:
                self.moveEdgePieces(self.green, edgePieceIndex)

            edgePieceIndex = self.checkEdgePieces(self.blue, 'white')
            if edgePieceIndex != -1:
                self.moveEdgePieces(self.blue, edgePieceIndex)

            edgePieceIndex = self.checkEdgePieces(self.orange, 'white')
            if edgePieceIndex != -1:
                self.moveEdgePieces(self.orange, edgePieceIndex)

            edgePieceIndex = self.checkEdgePieces(self.yellow, 'white')
            if edgePieceIndex != -1:
                self.moveEdgePieces(self.yellow, edgePieceIndex)

            temp += 1
            if temp >= 5:
                self.printCube()
                print()
            if temp == 10:
                print('could not form white cross after 10 tries')
                break

    def alignWhite(self): #gets proper edge alignment once white cross is in place
        temp = 0 #for debugging
        while self.red[7] != 'r' or self.blue[7] != 'b' or self.green[7] != 'g' or self.orange[7] != 'o':
            self.rotateCW(self.white)
            temp += 1
            if temp == 5:
                print("had to rotate more than 4 times")
                break


newCube = RegularAlgorithms()
# newCube.scrambleCube(505)
# newCube.getWhiteCross()
# newCube.printCube()
# newCube.getWhiteCross()

print()
print()
print()

newCube.scrambleCube(1100)
newCube.getWhiteCross()
newCube.alignWhite()

