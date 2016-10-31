"""
Creator: Peter Bynum
Sources:

"""

from random import randint
from ggame import App, Color, Frame, ImageAsset, LineStyle, Sprite, CircleAsset, RectangleAsset, EllipseAsset, PolygonAsset, TextAsset

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 300
#difficulty = input("Please choose a difficulty level: easy, medium, or hard")

easywords = ['monkey', 'toddler', 'cookies', 'image', 'shallow']
mediumwords = ['bandwagon', 'youthful', 'vaporize', 'pajama', 'whiskey']
hardwords = ['jazzy', 'abruptly', 'larynx', 'zephyr', 'rhubarb']

gallowsasset = ImageAsset("gallows.png",
        Frame(0,0,300,300), 7, 'vertical')

#letterbuttonasset
#wordbuttonasset

class Gallows(Sprite):

    def __init__(self, width, height):
        super().__init__(Gallows.asset, width, height)
        
        
class Hangman(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.gallows(gallowsasset = ImageAsset("gallows.png",
            Frame(0,0,300,300), 7, 'vertical')



myapp = Hangman(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
