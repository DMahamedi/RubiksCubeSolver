# RubiksCubeSolver

This is a program I am developing that automatically solve a Rubiks cube. It currently contains all the most important functionality needed to model and change the cube through rotations.
The plan is to use the base class to implement a variety of Rubiks cube solving techniques, with the first algorithms I am implementing being the Thistlewaite algorithm and the more generic beginner algorithms.

Cube.py contains the important functionalities which the algorithms will use to solve the cubes (namely the rotation function, since the rotations are very complex).
RegularAlgorithms.py is the class that will try to solve the cube using the generic algorithms which are the most easily-accessible on the internet.
ThistlewaiteCube.py does not yet contain any functionalities, but is intended to solve the cube using the Thistlewaite algorithm (which can solve the cube very quickly in less than 52 moves)

In the near future I plan to transition the program from using Python lists to NumPy arrays to make the code clearer and easier to understand.
Also being planned is a graphical user interface to visualize the cube and allow users to input their own cube states which the program can then solve.

