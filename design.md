# Head Soccer
Head Soccer was programmed in Python 3 using Brython.  It uses ggame as a graphics library.

The title screen consists simple of two sprites based on text assets, one for the words "Head Soccer!" and one for the words "Click to Continue."  The flashing quality of the "Click to Continue" is achieved by each frame changing the value of a variable and then destroying and recreating the sprite using the variable as the transparency value of the color of the text asset.  The same method is used later in the game with the words "Press Space to Continue" and "Press Space to Restart," and the same variable is used to store the transparency value.

In order to create the buttons, the game creates a list of integers from 0 to 8 and determines the position of the upper-left corner of each button using the following formula: ((x%3-1)/5*SCREEN_WIDTH+SCREEN_WIDTH/2-self.width/2, (x//3-1)/5*SCREEN_HEIGHT+SCREEN_HEIGHT/2-self.height/2), where x is the integer 0 to 8.  Each button is also assigned a color based on a list containing all the possible colors.  Once the screen is clicked, the game uses the position of the mouse click to determine which, if any button, was clicked.  It will then add the corresponding color to a list containing the colors for each player.  Resetting the colors clears this list.

Once the actual game begins, both the players and the ball will move each frame according to a velocity they are assigned.  Each frame, a constant representing the acceleration of gravity is added to the y-component of the velocities of both players and the ball.  However, if a player is on the ground, its velocity will be set to zero so that it does not leave the playing area.  Jumping sets the y-velocity of a player to give it upward movement.  Collision detection functions in ggame are used to determine when the ball collides with a goal, border, or player.  If the ball collides with a horizontal border or the top part of the goal (crossbar), it will multiply its y-velocity by -1, and it will multiply its x-velocity by -1 if it hits a vertical border.  If the ball and a player collide, their velocities will be set based on the following formulas: v'1 = (m1-m2)/(m1+m2)*v1 and v'2 = 2*m1/(m1+m2)*v1.

## Design Specification

The design specificaiton is a counterpart to the Functional Speciffication. Where a functional specification concerns itself
with inputs and outputs from the program, or the *experience* of a user running the program, the design specification is concerned with decisions that the engineer and programmer must make during its creation.

The design specification should include information like:

* What tools or frameworks will you use to build the project (e.g. http://runpython.com or ggame)?
* What language will you use for coding (usually Python 3)?
* For every element of the Functional Specification, what code will need to be written to support it?
* What data will be stored or manipulated by the program? How will it be encoded and organized?
* Describe the logic and/or code behind every interaction with the user, and behind everything displayed.
* If your program uses an unusual or notable *algorithm*, what is the algorithm and how does it work?
