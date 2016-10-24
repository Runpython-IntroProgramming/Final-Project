# Hangman



## Functional Specification

This project is a python implementation of Hangman. It is accessed via runpython.com. The program is a single graphics screen that will update after inputs by the user. When the user first starts the program, they are presented with an empty gallows and a certain number of blanks depending on the number of letters in the word-to-be-guessed. When the user is ready, he can press a "Guess a letter!" button. Once this button is pressed, an input popup appears where the user will make his guess. If he guesses correctly, the letter will replace the blanks. Otherwise, a "step" is added to the gallows and the letter appears at the bottom of the screen along with all the other incorrect guesses. If the user thinks he is ready to guess the entire word, he can press the "Guess the word!" button. Another popup will appear where the guess is made. If the user guesses correctly, the program will tell the user (via another popup) that he or she has won. Otherwise, it will add another "step" to the gallows and continue playing. If the Hangman is fully constructed, the man falls and the words "You Lose" appear on the screen. The Hangman and gallows is a set of graphical assets. All words/letters are text assets.
