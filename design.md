Draw me a Picture!

## Design Specification
I will use runpython and the ggame library. This will utilize Python 3.
The whole program is contained in a file called "final.py" which recalls several images stored in the corresponding folders within the repository; and functions from the ggame folder.

The program starts by defining the screen dimensions and then a list of colors (black, white, turqoise, orange, purple, pale/peach-colored; light green, and brown. Then it defines two line styles.
Then the program creates two empty list and sets two global variables to preset values: "stage" to 1 and "color" to 0.
It then proceeds to create 11 graphical assets: 7 circles, 1 rectangle, and 3 textassets. These are all placed on the screen later on.

Then it creates a class "Icon" which will later have subclasses. Icon's init function has the arguments: self, asset, position, and prop. The init function includes setting several variable to their default values, calling the class' default init function via super().__init__ , and setting its center to its graphical center (0.5,0.5).
Next, it sets a condition based on an argument defined when creating a sprite: "prop" standing for property (of the sprite). When this is true, the program will consider it what I call an icon (lowercase, not to be confused with "Icon"). For only the icons where prop is marked as true, the init function says for the program to listen for the mouse-event "mousedown".
If prop == False, however, the corresponding sound will be played thru the speakers.
The "mousedown" event has a number of steps. It starts by saying that the variable stage is global before calculating the length of the list 'clkun'. Two of the variables the program uses are stage and 'self.ct'. stage defines which stage of the program the program is in, so it starts in stage 1. ct (or self.ct) counts how many times the mouse has been clicked.
Then, if stage==1, it checks for whether ct is an even or odd number. If ct is odd -- calculated by "if (self.ct)%2 == 1", then it calculates the absolute value of the differnce between first the x, and then the y; of the mouse and the given sprite.
It uses the variables self.b and self.c to calculate whether the mouse is close to the sprite in first the x and then the y directions. If both "b" and "c" are equal to 2 (ie the mouse is within 40 pixels of the sprite in both directions), it records the coordinates of the mouse and the subclass of the sprite: type(self), in the list clkun.
If ct is even, so the opposite of the condition for it being odd, it will set the variable "chk" to the last entry in 'clkun'. Then if the last entry in the list "clkun" is equal to the subclass of the sprite being referenced, it will add the coordinates of the mouse to the list clkdx. Finally, it will create a sprite of the subclass listed in the last entry of clkun at the location listed in the last entry of clkdx. This sprite does NOT have its "prop" value equal to true.
Finally, the mouse-event increases self.ct by 1, indicating the mouse has been clicked and that click has been processed.
Then the program creates the subclasses for 6 kinds of icons: a boy, bird, bunny, cat, tree, and flower. It uses the appropriate image from the image folder and super().__init__ to recall the "Icon" class' init function, to create its own init function.
It then sets the scale for the subclass, so that the sprites do not appear too large or small relative to each other.
A sound file is referenced at the end of each subclass, so it is played when a non-"icon" sprite of the subclass is created.

For its last class, the program creates the class Draw(App) which places all of the graphics on the screen. This class starts with its init function which has the arguments self, width, and height. It then proceeds to call stage a global variable and recalls the default app class' init function using super().__init__
After displaying a message welcoming the user, the program places 8 sprites on the left side of the screen: the six inital icons, a box separating them from the remaining portion of the screen, and a label reading "Icons".
Then it directs the App to listen for 15 key-events and 3 mouse-events: there are 8 "keydown" events and 7 "keyup" events.
The 8 keydown events are for the keys 'enter', 'q', 'r', 'o', 'p', 'g', 'l', 'b'. Pressing the enter key triggers an event named switch, while the other keys trigger events named for colors: 'q' is for turq (ie turquoise), 'r' is for brn (brown),  'o' is for orange, 'p' is for purp (ie purple), 'g' for green, 'l' for pale (a light yellow), and 'b' for black.
The 7 key down events are for when the same 7 letter keys are released and they all trigger the same event called no_col. This event sets the variable color to 0 (if stage == 2).
The first event it defines however, is the event 'switch'. Switch increases the variable stage whenever the 'return' key is pressed. This allows the program to switch from dragging and droppuing sprites for stage==1 to drawing on the screen with stage==2 (the user is notified of this as well). 
When stage is increased to 3, all graphical actions are disabled and a message about a message explaining that the program is over is displayed on the graphics tab.
When stage is increased to 4, the message trigger when stage == 3 is turned invisible. 
The events mse_isdn and mse_no simply indicate whether the mouse is pressed or not by setting Draw.a to 1 or 0, respectively.
The event move says that whenever the mouse's coordinates change, to set msx to event.x and msy to event.y.
Next, the 7 color events all state that color is a global variable. They are named green, turq, orange, black, purp, brn, and pale; which, if stage == 2, set color to 1, 2, 3, 4, 5, 6, and 7, respectively.
After the aforementioned event no_col is defined, the step function is defined. This function starts by naming color as a global variable before having an if loop that only activates if the mouse is pressed down (a==1) and color is not equal to 0.
Then, if color == 1 it places a green dot where the mouse was most recently placed, if color == 2, it places a turquoise one; if color == 3, it places an orange dot; if color == 4 a larger, black dot; if color == 5, a purple dot; if color == 6, a brown dot; and if color == 7, a light yellow dot. This is all done using the assets defined at the very beginning of the program.
Nexy, it creates my_draw as a version of Draw with the desired screen dimensions as set at the beginning of the program. It then executes my_draw.


images: https://s-media-cache-ak0.pinimg.com/originals/d8/d9/59/d8d9596f8e39f135f86a01f61d381eec.jpg, https://s-media-cache-ak0.pinimg.com/originals/d8/d9/59/d8d9596f8e39f135f86a01f61d381eec.jpg; http://orig14.deviantart.net/7b77/f/2013/203/5/5/cartoon_boy_by_navdbest-d6ekjw9.png
http://cartoon-birds.clipartonline.net/_/rsrc/1472868952735/blue-birds-cartoon-bird-images/blue_bird_clipart_image_9.png?height=320&width=320 .
-sounds have been made by yours truly
