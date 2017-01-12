# Simple Raycaster

## Design Specification

I will use runpython to build the program. It will use Python 3. For the level editor in the corner, the program will use a list to track what squares are selected. This Library will carry over to the walls which are detected. The walls will be detected by a "ray" which will start at the library for the players position and detect all tiles between that position and the first tile in the line of the ray. There will need to be movement sections in the code which work off of key presses. There will also be a loop for displaying the 3D graphics. This will need another loop in it for the ray which detects walls to continue to grow longer until it hits a wall. 
