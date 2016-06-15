# Head Soccer
Head Soccer was programmed in Python 3 using Brython.  It uses ggame as a graphics library.

The title screen consists simple of two sprites based on text assets, one for the words "Head Soccer!" and one for the words "Click to Continue."  The flashing quality of the "Click to Continue" is achieved by each frame changing the value of a variable and then destroying and recreating the sprite using the variable as the transparency value of the color of the text asset.  The same method is used later in the game with the words "Press Space to Continue" and "Press Space to Restart," and the same variable is used to store the transparency value.

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
