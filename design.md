Hangman

## Design Specification

The design specificaiton is a counterpart to the Functional Speciffication. Where a functional specification concerns itself
with inputs and outputs from the program, or the *experience* of a user running the program, the design specification is concerned with decisions that the engineer and programmer must make during its creation.

The design specification should include information like:

* What tools or frameworks will you use to build the project (e.g. http://runpython.com or ggame)?

The program runs on runpython.com and uses ggame. The gallows and buttons visual assets were created using Adobe Illustrator.

* What language will you use for coding (usually Python 3)?

The code is in the language of Python 3.

* For every element of the Functional Specification, what code will need to be written to support it?

To support the elements of the Functional Specification, the program imports many things from ggame. At the beginning of the program, the colors black, blue, green and red are all defined, as well as a line style. These colors and line style is used to create the Sprites later on. For each visual in the the game (the background, gallows, buttons, and text), there is an asset and then a Sprite created in the init of the class Hangman. Some of the sprites use assets already available in ggame (background is a rectangle asset, text is a text asset). The buttons and gallows are made using image assets which I created in Adobe Illustrator. Many of the sprites are updated throughout the rest of the game in accordance with what the user inputs. Neither the background nor the buttons change throughout the game. The gallows use the setImage function, because the asset is actually a series of gallow each with differing numbers of "body parts". The unknown word and the guessed letters are both only one text sprite. With each input by the user, the sprite is destroyed and replaced with a new text asset that uses an updated string. The "You Won" text is a simple text asset that appears once the user has won the game. The "You Lose" text is a part of the final frame of the gallows image asset.

* What data will be stored or manipulated by the program? How will it be encoded and organized?

As described above, many colors and assets are stored for the visual aspects of the program. Other data that is stored includes:

difficulty: the difficulty is input by the user at the beginning of the program. Depending on what is input, a random word is chosen from the diffculy's corresonding list (below)

easy: the list of easy words

medium: the list of medium words

hard: the list of hard words

word: the chosen word from the list

wordinprogress: This is a string containing at first only a number of underscores equal to the number of letters in "word". It is updated to contain letters and words if the user makes a correct guess.

displayedword: This is the string that is used in the TextAsset for the word on the program. It is identical to "wordinprogress" except that is has spaces inbetween the underscores to make the sprite easier to read (if the spaces weren't included, the user would not be able to tell how many letters the word has, because the underscores would form a single line).

finishedword: this is the finished word, identical to "word" except with the same spacing as in "displayed word". The program checks it against "displayed word" to see if the user has completed the word.

allsymbols: This is a list of symbols that the program checks against to prevent the user from guessing anything but letters.

alreadyguessed: This is a list of all the letter that have already been guessed by the user

alreadyguessedstring: This is a string built off of "alreadyguessed" that is used by the text asset that displays already guessed letters on the graphics screen.

mousex: This is the x coordinate of the mouse. It is updated continually with each step to check if the mouse is over one of the button sprites.

mousey: This is the y coordinate of the mouse. It is updated continually with each step to check if the mouse is over one of the button sprites.



To see how the strings are encoded, see the algorithm.

* Describe the logic and/or code behind every interaction with the user, and behind everything displayed.



* If your program uses an unusual or notable *algorithm*, what is the algorithm and how does it work?

One algorithm that is used many times is the "for x in range(len(word))...". I used this algorithm to "build" the strings that are used by the text assets to display the word on the screen as it is decoded. For every letter in the hidden word, the program adds on to a string. At the beginning it only adds "_". Later on, this changes to letters if the user inputs the correct letter. This is done by "if word[x] == guessedletter, then use guessedletter instead of "_".
