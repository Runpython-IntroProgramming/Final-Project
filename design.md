# Block Game (single or multiplayer)

## Design Specification

The design specificaiton is a counterpart to the Functional Speciffication. Where a functional specification concerns itself
with inputs and outputs from the program, or the *experience* of a user running the program, the design specification is concerned with decisions that the engineer and programmer must make during its creation.

The design specification should include information like:

* What tools or frameworks will you use to build the project (e.g. https://runpython.org or ggame)?
* What language will you use for coding (usually Python 3)?
* For every element of the Functional Specification, what code will need to be written to support it?
* What data will be stored or manipulated by the program? How will it be encoded and organized?
* Describe the logic and/or code behind every interaction with the user, and behind everything displayed.
* If your program uses an unusual or notable *algorithm*, what is the algorithm and how does it work?

* This Program was made using ggame
* To make the sprite (or sprites) I made 5 classes, person, top, botton, Sideleft and Sideright
* Using the arrow keys (and XCD in double player) I programed the sprites to move together based on these inputsin the Game App outside of the step function
  * Here the code also keep the jump (up arrow or D) from working unless the sprite is in contact with the ground
* In the step is where all the colisions are checked
  * If the bottom is coliding with a black block (the grid) then it will not move down more
  * If the top is coliding with a black block the sprite.y will adujust inself the halt the colision
  * If a side is coliding with a black block it will adjust sprite.x to no longer be coliding
  * If the person is coliding with a gem then gem.destroy(), and the #Gems will change
  * If the bottom is coliding with a spike then the sprite will die
* The Program stores:
  * The # Gems collected (gemgot = #)
  * The living state of the sprite (dead = True or False)
  * The if the bottom of the sprite is coliding with the ground (grounded = True or False)
  * If the game is over (gameover = True or False)
* The code is based on the basic input of the user from the designated keys
* The grade output at the end is designated by the number of gems collected
