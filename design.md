snake Game. 

## Design Specification

I used runpython and ggame to create this game. The program which works is snake3.py. I used the language python 3. To make the snake move I wrote a step function. To make it respond to different keys being pressed I wrote def (event) things. For the arrow keys they would change a variable which would then determine the direction the snake would move. I had a variable x, which would effect the x position of the front of the snake and a variable y which does the same for the y. Depending on which direction the snake was going it would change the x or y variable by 20. Then I would add a sprite to a list at the coordinates (x,y), and add (x,y) to a list called snk or snak which has all of the coordinates of all of the pieces to the snake. I would then delete the first sprite in the first list, and the first numbers in the second list. This gives the pieces the apearance of moving. When the snake hits one of the blue dots, it detects this through lists. The same type of thing happens as normal, except nothing is deleted from the two lists. this makes the snake 1 longer than it was before. If the snake's Head's x position or y position is greater than the dimensions of the screen or they are the same as another part of the snake then a variable lose=true and the everything will cease to happen. I also created two lists called blck or something like that. These contain information for red sprites which the x and y variable will check. If the x and y is the same as the coordinates in those list the variable lose =true. The lists are controlled when b is pressed and then another sprite and it's coordinates are added to their respective list. 

* What tools or frameworks will you use to build the project (e.g. http://runpython.com or ggame)?
* What language will you use for coding (usually Python 3)?
* For every element of the Functional Specification, what code will need to be written to support it?
* What data will be stored or manipulated by the program? How will it be encoded and organized?
* Describe the logic and/or code behind every interaction with the user, and behind everything displayed.
* If your program uses an unusual or notable *algorithm*, what is the algorithm and how does it work?
