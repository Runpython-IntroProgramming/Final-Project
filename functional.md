# Head Soccer

This is a version of the popular game "Head Soccer," in which two players attempt to hit a soccer ball into an opposing goal while defending their goal in a two-dimensional world.  This version is perhaps more related to "Slime Soccer," which is a more simplified version of the game.

The game can be played in browser via Brython at the following link: http://runpython.com/?user=davidwilson826&repo=Final-Project&name=HeadSoccer.py.  No installation is required.

Once the game is initially loaded, it will display a simple title screen which says "Head Soccer!" and below that, "Click to Continue."  Clicking anywhere on the screen will bring the player to a screen with colored buttons where each player can select his/her player color.  Player 1 selects first, and player 2 will select second.  After one or both players have selected a color, a message will appear telling the players that they can hit the "q" key to change colors.  If either player wishes to change color, he/she can press "q," which will reset both colors and begin the color selection process again with player 1.  Once both players have selected colors, a message saying "Press Space to Begin" will appear.  Pressing space will initiate the game.

At this point both players will appear as semicircles of their chosen colors.  Player 1 will be on the left and player 2 on the right.  The playing area is enclosed by black borders, and on each side there is a black rectangle representing a goal.  The remaining game time in minutes and seconds will also be displayed in the center of the screen.  Additionally, player 1's score will be displayed near the left goal and player 2's near the right goal.  A black circle representing the ball will appear at the center of the screen.

Player 1 can move left, move right, and jump using the "a," "d," and "w" keys respectively.  Player 2 uses the left and right arrow keys to move in the corresponding directions and uses the up arrow to jump.  Players can only jump if they are touching the ground (they cannot jump a second time while in the air) and cannot exit the playing area.  However, they are allowed to adjust their horizontal movement in midair.

The ball will be affected by the force of gravity and will bounce whenever it hits a border or the top portion of a goal (as if hitting a crossbar).  Additionally, in the event of a collision with either player, it and the player involve will change velocity.  If the ball hits either goal, a player will be awarded a point.  Player 1 scores by hitting the ball into the right goal and player 2 scores on the left goal.  Thus, the object of the game is to move the player to hit the ball into the opposing goal while also attempting to defending the other goal.

In the event of a goal, the text "Goal!" will appear in the center of the screen, and the score of the player who got the goal will increase by one.  Play will continue normally for two seconds, but neither player may score during this time.  Afterwards, the "Goal!" text will disappear, the ball and players will reset to their initial positions, goals can again be scored, and normal play will continue.

After the game time has reached zero, the ball and players will freeze, even if keys are still pressed.  Whichever player has scored more goals by this time is the winner, and text will appear stating who that was.  In the event that the scores are the same, the game will declare a draw.  The text "Press Space to Restart" will also appear.  Pressing space will return to the color selection screen, at which point players can select colors and play again.

## Functional Specification

This document should become the functional specification of the project you are working on.

A functional specification describes in great detail how a device or program will appear to an
outside user. That is, it treats all hardware as a "black box", the contents of which are completely
unknown to the user. The functional specification should include sections with the following information:

Your specification **should include** the following types of information:

* A title. Replace the title at the beginning of this document.
* Summary or introduction. In general, in a few lines or less, what is your program about or what is it about?
* How does the user access your program? Is it shared via http://runpython.com? Is a web site? Embedded in 
  a single board computer? 
* If there are graphics screens involved, describe every screen that the user will experience: what is it for? 
  What did the user have to do to get there and how does she move on to the next?
* For each graphics screen, describe every active control input and what it does. What elements on the screen will
  change in response to user input?
* Does the program respond to mouse input? What, exactly, does the mouse do?
* Does the program respond to keyboard input? How?
* What graphical assets will be used?
* Does the user have to do anything to install the program?

Your specification should **not** include the following types of information:

* The language you will use to create it.
* Names of any specific files in the project.
* How you will structure the classes, functions and code in your program.
* The name of any files or tools that you will use to design the program.
