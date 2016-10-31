"""
Creator: Peter Bynum
Sources:

"""

from random import randint
from ggame import App, Color, Frame, ImageAsset, LineStyle, Sprite, CircleAsset, RectangleAsset, EllipseAsset, PolygonAsset, TextAsset

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
#difficulty = input("Please choose a difficulty level: easy, medium, or hard")

easywords = ['monkey', 'toddler', 'cookies', 'image', 'shallow']
mediumwords = ['bandwagon', 'youthful', 'vaporize', 'pajama', 'whiskey']
hardwords = ['jazzy', 'abruptly', 'larynx', 'zephyr', 'rhubarb']

gallowsasset = ImageAsset("gallows.png",
        Frame(0,0,300,300), 7, 'vertical')

#letterbuttonasset
#wordbuttonasset

class Hangman(App):
    bgasset = RectangleAsset(width, height, noline, 
    def __init__(self, width, height):
        super().__init__(width, height)
        self.gallows = Sprite(gallowsasset,(300,0))
        self.gallows.scale = 1.5





myapp = Hangman(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
