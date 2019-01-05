# Compact Personal Planner in Python



## Functional Specification

This is a planner program which records and displays user-inputted tasks based on their subject category and date. The list of subjects is customizable, and the planner will display the list of tasks dated after a user-selected date.

The planner is accessed via downloading the project at https://github.com/chenmasterandrew/Final-Project and running main.py.

Upon running main.py, the user is greeted with the main screen of the program, with the current date displayed displayed in the center, a list of tasks dated after the current date displayed above, and a calendar listing out the previous, current, and next two weeks of dates displayed below. The user can modify the tasks displayed by changing the selected date (default is the current date) by clicking on a different date on the bottom calendar, and the list of tasks will change to list only the tasks that occur after the selected date. In addition, there are buttons in the top left and top right of the screens. Upon clicking on a button, the user taken to the left or right screen, respectively.

On the right screen, the user can see the planner's recognized list of subjects towards the top of the screen. In the center, the user can click on the query field, input the name of a subject with keyboard input, and add a subject if it does not already exist by clicking the "+" button, or remove a subject if the subject already exists by clicking the "-" button. The list of subjects above will update to reflect any changes that the user makes in the query field. The user can return to the main screen by clicking the button in the top left.

On the left screen, the user can input new tasks into the planner through the three query fields. The user can input a subject in the top query field by clicking on the field and using keyboard input. Pressing enter will autocomplete the user's input to match a previously inputted subject from the subject list on the right screen and confirm the subject the user wishes to input. The user can input a date for the task in the center query field by clicking on the field and using keyboad input. Pressing enter will autocomplete the user's input into a formalized numerical date and confirm the date the user wishes to input. The program will autocomplete numerical dates (1/7/19), numerical dates without years (1/7), days of the week (today, tomorrow, Monday), and days of the week preceded with the word "next" (next Monday). Finally, the user can input the name of the task in the bottom quary field by clicking on it and using keyboard input. Pressing enter in the bottom field when the subject and date have been entered as well will enter a new task, which will appear on the main screen. The user can return to the main screen by clicking the button in the top right.

The planner also features a set of backgrounds which can cycled by using the "f" key on the main screen.
