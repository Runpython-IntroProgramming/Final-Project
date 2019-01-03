# Block Game (single or multiplayer)

## Design Specification

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
