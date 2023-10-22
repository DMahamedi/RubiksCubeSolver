# RubiksCubeSolver

This is a program I am developing that automatically solve a Rubiks cube. Cube.py is the base class that contains all of the most important functionality to rotate, modify, and model the cube. The plan is to use the base class to implement a variety of Rubiks cube solving techniques, with the first algorithms I am implementing being the Thistlewaite algorithm and the more generic beginner algorithms.

Right now, the program is able to solve the  ***entire cube*** using the most common beginner algorithms within RegularAlgorithms.py

Cube.py contains the important functionalities which the algorithms will use to solve the cubes (namely the rotation function, since the rotations are very complex).

RegularAlgorithms.py is the class that solves the cube using the generic algorithms which are the most easily-accessible on the internet.

ThistlewaiteCube.py does not yet contain any functionalities, but is intended to solve the cube using the Thistlewaite algorithm (which can solve the cube very quickly in less than 52 moves)

In the near future I plan to transition the program from using Python lists to NumPy arrays to make the code clearer and easier to understand.
Also being planned is a graphical user interface to visualize the cube and allow users to input their own cube states which the program can then solve.

# Pictures

### Using the following code solves the cube in a three-step process
```

cube = RegularAlgorithms()
cube.scrambleCube(1000) #1000 random moves to scramble the cube
print('The cube has been randomized: ')
cube.printCube()
print('-----------------------')
```

![Cube is first randomized](WorkingPictures/CubeRandomized.png)
```
cube.solveWhiteLayer() #solves first layer
print('First layer solved: ')
cube.printCube()
print('-----------------------')
```
![Program solves the first layer](WorkingPictures/FirstLayerSolved.png)
```
cube.solveMiddleLayer() #solves second layer
print('Second layer solved: ')
cube.printCube()
print('-----------------------')
```
![Program solves the second layer](WorkingPictures/SecondLayerSolved.png)
```
cube.solveYellowLayer() #solves third and final layer
print('The cube is solved: ')
cube.printCube()
```
![Program finishes solving the cube](WorkingPictures/CubeSolved.png)

### There is also a master function to entirely automate the solution process
```
cube = RegularAlgorithms() #creating the cube
cube.scrambleCube(1000) #scrambles the cube for 1000 randomized moves
print("Randomized cube: ")
cube.printCube()
print('-----------------------')
```
![Cube randomized](WorkingPictures/CubeRandomized_V2.png)
```
cube.solveCube()
print("Solved cube: ")
cube.printCube()
```
![Cube solved](WorkingPictures/CubeSolved_V2.png)

