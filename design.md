Hangman

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

The program runs on runpython.com and uses ggame. The gallows and buttons visual assets were created using Adobe Illustrator. The code is in the language of Python 3. For each visual in the the game (the background, gallows, buttons, and text), there is an asset and then a Sprite created in the init of the class Hangman. They are then updated throughout the rest of the game in accordance with what the user inputs:
*the background does not change
*the buttons do not change
*the gallows use the setImage function, because the asset is actually a series of gallow each with differing numbers of "body parts"
*the unknown word and the guessed letters are both only one sprite. 
