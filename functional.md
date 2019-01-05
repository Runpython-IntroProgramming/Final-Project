# Compact Personal Planner in Python



## Functional Specification

This is a planner program which records and displays user-inputted tasks based on their subject category and date. The list of subjects is customizable, and the planner will display the list of tasks dated after a user-selected date.

The planner is accessed via downloading the project at https://github.com/chenmasterandrew/Final-Project and running main.py.

Upon running main.py, the user is greeted with the main screen of the program, with the current date displayed displayed in the center, a list of tasks dated after the current date displayed above, and a calendar listing out the previous, current, and next two weeks of dates displayed below. The user can modify the tasks displayed by changing the selected date (default is the current date) by clicking on a different date on the bottom calendar, and the list of tasks will change to list only the tasks that occur after the selected date. In addition, there are buttons in the top left and top right of the screens. Upon clicking on a button, the user taken to the left or right screen, respectively.

On the right screen, the user can see the planner's recognized list of subjects towards the top of the screen. In the center, the user can click on the query field, input the name of a subject with keyboard input, and add a subject if it does not already exist by clicking the "+" button, or remove a subject if the subject already exists by clicking the "-" button. The list of subjects above will update to reflect any changes that the user makes in the query field. The user can return to the main screen by clicking the button in the top left.

On the left screen, the user can input new tasks into the planner through the three query fields. The user can input a subject in the top query field by clicking on the field and using keyboard input. 



A functional specification describes in great detail how a device or program will appear to an
outside user. That is, it treats all hardware as a "black box", the contents of which are completely
unknown to the user. The functional specification should include sections with the following information:

Your specification **should include** the following types of information:

* A title. Replace the title at the beginning of this document.
* Summary or introduction. In general, in a few lines or less, what is your program about or what is it about?
* How does the user access your program? Is it shared via https://runpython.org? Is a web site? Embedded in 
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
