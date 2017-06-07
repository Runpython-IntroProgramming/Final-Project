snake Game. 

## Design Specification

The design specificaiton is a counterpart to the Functional Speciffication. Where a functional specification concerns itself
with inputs and outputs from the program, or the *experience* of a user running the program, the design specification is concerned with decisions that the engineer and programmer must make during its creation.

The design specification should include information like:

I used runpython and ggame to create this game. The program which works is snake3.py. I used the language python 3. To make the snake move I wrote a step function. To make it respond to different keys being pressed I wrote def (event) things. For the arrow keys they would change a variable which would then determine the direction the snake would move. I had a variable x, which would effect the x position of the front of the snake and a variable y which does the same for the y. Depending on which direction the snake was going it would change the x or y variable by 20. Then I would add a sprite to a list at the coordinates (x,y), and add (x,y) to a list called snk or snak which has all of the coordinates of all of the pieces to the snake. I would then delete the first sprite in the first list, and the first numbers in the second list. This gives the pieces the apearance of moving. When the snake hits one of the blue dots, it detects this through lists. The same type of thing happens as normal, except nothing is deleted from the two lists. this makes the snake 1 longer than it was before. If the snake's Head's x position or y position is greater than the dimensions of the screen or they are the same as another part of the snake then a variable lose=true and the everything will cease to happen. 

* What tools or frameworks will you use to build the project (e.g. http://runpython.com or ggame)?
* What language will you use for coding (usually Python 3)?
* For every element of the Functional Specification, what code will need to be written to support it?
* What data will be stored or manipulated by the program? How will it be encoded and organized?
* Describe the logic and/or code behind every interaction with the user, and behind everything displayed.
* If your program uses an unusual or notable *algorithm*, what is the algorithm and how does it work?
