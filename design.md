# Minesweeper Game 

## Design Specification

Description: A simple text-based implementation of the classic game Minesweeper

Usage: python ./minesweeper.py [--width] [--height] [--mines] [-h --help]
optional arguments: -h, --help show this help message and exit --width WIDTH the width of the minesweeper board (default: 10) --height HEIGHT the height of the minesweeper board (default: 10) --mines MINES the number of mines to place on the board (default: 15)

I used the text editor named PyCharm to create this game and ran it through the mac terminal.
This python code runs recurrent main loop every time you press a key to determine whether the space is a mine, number, or empty space. 
By pressing various keys, the user can perform certain functions such as f to flag a space, r to restart, or q to quit the game.
The code takes the input from the keyboard and uses a respond function to edit a given space. The display function then refreshes the board and the user can make another move. 
The curses function enables the user to move throuhought the display board and make edits in real time very easily. Every time enter, f, r, or q are pressed, the board will change in a specific way.
