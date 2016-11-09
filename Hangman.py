"""
Creator: Peter Bynum
Sources: https://www.tutorialspoint.com/python/python_strings.htm

"""

from random import randint
from ggame import App, Color, Frame, ImageAsset, LineStyle, Sprite, CircleAsset, RectangleAsset, EllipseAsset, PolygonAsset, TextAsset

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

blue = Color(0xcce6ff, 1.0)
black = Color(0x000000, 1.0)
green = Color(0x00cc00, 1.0)
noline = LineStyle(0,blue)
gallowsasset = ImageAsset("gallows.png",
        Frame(0,0,300,300), 7, 'vertical')
guessletterasset = ImageAsset("guessletterasset.png")
wordbuttonasset = ImageAsset("guesswordasset.png")

difficulty = input("Please choose a difficulty level: easy, medium, or hard")

easy = ['monkey', 'toddler', 'cookies', 'image', 'shallow']
medium = ['bandwagon', 'youthful', 'vaporize', 'pajama', 'whiskey']
hard = ['jazzy', 'abruptly', 'larynx', 'zephyr', 'rhubarb']

if difficulty=='easy':
    word = str(easy[randint(0,4)])
if difficulty=='medium':
    word = str(medium[randint(0,4)])
if difficulty=='hard':
    word = str(hard[randint(0,4)])
print(word)

wordinprogress = ''
for x in range(len(word)):
    wordinprogress = wordinprogress + '_'

displayedword = ''
for x in range(len(wordinprogress)):
            displayedword = displayedword + "{0:<3}".format(wordinprogress[x])

alreadyguessed = []
alreadyguessedstring = ''

wordasset = TextAsset(displayedword, style='60px Helvetica',align='center',width=1000)
guessedasset = TextAsset(alreadyguessedstring, style='12px Helvetica',align='center',width=100)
winscreenasset = TextAsset('You Won!', style='200px Helvetica',align='center',width=1000, fill=green)

class Hangman(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        #creating sprites
        bgasset = RectangleAsset(SCREEN_WIDTH, 700, noline, blue)
        Sprite(bgasset,(0,0))
        self.gallows = Sprite(gallowsasset,(350,50))
        self.gallows.scale = 1.5
        self.letterbutton = Sprite(guessletterasset,(800,250))
        self.wordbutton = Sprite(wordbuttonasset,(800,300))
        self.gallows.hangingphase = 0
        self.wordsprite = Sprite(wordasset,(500,525))
        self.wordsprite.fxcenter = 0.5
        self.guessedsprite = Sprite(guessedasset, (100,250))
        
    #tracking mouse
    def mousemove(self, event):
        global mousex
        global mousey
        mousex = event.x-10
        mousey = event.y-10
    
    #sensing clicks
    def mousedown(self, event):
        global mousex
        global mousey
        if (mousex >= 800 and mousex <= 840) and (mousey >= 250 and mousey <= 275):
            self.guessletter()
        if (mousex >= 800 and mousex <= 840) and (mousey >= 300 and mousey <= 325):
            self.guessword()

    def guessletter(self):
        global wordinprogress
        global word
        global displayedword
        global wordsprite
        global alreadyguessedstring
        global guessedasset
        global wordasset
        global hangingphase
        global gallows
        global guessedsprite
        displayedword = ''
        guessedletter = input('Please guess a letter!')
        
        while alreadyguessed.count(guessedletter) > 0:
            guessedletter = input('You already guessed that letter! Try again:')
        
        if word.count(guessedletter) > 0:
            for x in range(len(word)):
                if guessedletter == word[x]:
                    wordinprogress = wordinprogress[:x] + "{0}".format(guessedletter) + wordinprogress[x+1:]
            for x in range(len(wordinprogress)):
                displayedword = displayedword + "{0:<3}".format(wordinprogress[x])
            self.wordsprite.destroy()
            wordasset = TextAsset(displayedword, style='60px Helvetica',align='center',width=1000)
            self.wordsprite = Sprite(wordasset,(500,525))
            self.wordsprite.fxcenter = 0.5
            alreadyguessed.append(guessedletter)
            alreadyguessedstring = alreadyguessedstring + "{0:<3}".format(guessedletter)
        else:
            alreadyguessed.append(guessedletter)
            alreadyguessedstring = alreadyguessedstring + "{0:<3}".format(guessedletter)
            self.gallows.hangingphase += 1
            self.gallows.setImage(self.gallows.hangingphase)
            
        print(alreadyguessedstring)
        self.guessedsprite.destroy()
        self.guessedsprite = Sprite(guessedasset, (100,250))
        print('printed')


    
    def guessword(self):
        global word
        global hangingphase
        global gallows
        guessedword = input("Guess the word!")
        if guessedword == word:
            endscreen = Sprite(winscreenasset, (250,250))
        else:
            self.gallows.hangingphase += 1
        self.gallows.setImage(self.gallows.hangingphase)
        
    def endgame(self):
        if self.gallows.hangingphase == 6:
            unlistenMouseEvent('mousemove', myapp.mousemove)
            unlistenMouseEvent('mousedown', myapp.mousedown)


myapp = Hangman(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenMouseEvent('mousemove', myapp.mousemove)
myapp.listenMouseEvent('mousedown', myapp.mousedown)
myapp.run()
