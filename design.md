# Simon

## Design Specification

I used runpython.org, ggame, and time to build this project using the language of Python 3. 

The design specificaiton is a counterpart to the Functional Speciffication. Where a functional specification concerns itself
with inputs and outputs from the program, or the *experience* of a user running the program, the design specification is concerned with decisions that the engineer and programmer must make during its creation.

Unbounded, the step function loops very quickly, but in order to create the graphics of my program, I had to use time. Whenever the program loops through the step function, the time is recorded at the very beginning. Then, once completed, the step function will take the time again. The step function will continue looping, checking the time, until the appropriate amount of time has elapsed between when the time was originally set and the current time. The time the program must wait can be manipulated by changing the variable self.waittime. This system allows me to create graphics such as buttons lighting up. I set them to normal, then lit, then normal again, waiting between each state. 

To accomplish the game, I manipulated the variable self.state. Each time the program loops the step function, self.state can be changed. Thus, self.state can be "lit" meaning that I want the buttons to light up. Then, within the portion of the code that runs when self.state is "lit", I can set the state to "unlit". The program will run the "lit" section, wait the appropriate amount of time, then run the "unlit" section, creating the buttons lighting up then returning to normal. From there, self.state can be a number of other things including "record" which executes the portion of the code that checks for user input. 

To create and check the Simon pattern, I used a list. The list begins with a randomly generated number between 1 and 4. Each of these numbers corresponds to a different color. My code checks to see which number is chosen, then runs the code to light up the appropriate button. Then, the user is asked to respond. The user creates their own list by clicking on the screen. Based on which region of the screen the user clicks, the code determines the corresponding button and corresponding number, and adds that number to the list. The program then checks the first number in both lists to ensure they're the same. Next, the computer's list is appended with another number between 1 and 4, and the same mechanism is executed again. 

The design specification should include information like:

* For every element of the Functional Specification, what code will need to be written to support it?
* What data will be stored or manipulated by the program? How will it be encoded and organized?
* Describe the logic and/or code behind every interaction with the user, and behind everything displayed.
* If your program uses an unusual or notable *algorithm*, what is the algorithm and how does it work?
