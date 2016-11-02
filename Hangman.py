"""
Creator: Peter Bynum
Sources:

"""

from random import randint
from ggame import App, Color, Frame, ImageAsset, LineStyle, Sprite, CircleAsset, RectangleAsset, EllipseAsset, PolygonAsset, TextAsset

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

blue = Color(0xcce6ff, 1.0)
black = Color(0x000000, 1.0)
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

"""
print(word)
print(len(word))

for x in range(len(word)):
    if word
wordinprogress = 

"""
wordasset = TextAsset(word, style='60px Helvetica',align='center')

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
        self.wordsprite = Sprite(wordasset,(500,500))
        
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
            Hangman.guessletter()
        if (mousex >= 800 and mousex <= 840) and (mousey >= 300 and mousey <= 325):
            Hangman.guessword()

    def guessletter():
        guessedletter = input("Please guess a letter (lowercase): ")
    
    def guessword():
        print('guessingword')
    

            




myapp = Hangman(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenMouseEvent('mousemove', myapp.mousemove)
myapp.listenMouseEvent('mousedown', myapp.mousedown)
myapp.run()
