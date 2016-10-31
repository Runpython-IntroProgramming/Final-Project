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

class Gallows(Sprite):
    asset = ImageAsset("gallows.png",
        Frame(0,0,300,300), 7, 'vertical')
    def __init__(self, width, height):
        super().__init__(Gallows.asset, width, height)
        
        
class Hangman(App):
    asset = ImageAsset("gallows.png",
        Frame(0,0,300,300), 7, 'vertical')
    def __init__(self, width, height):
        super().__init__(width, height)
        Sprite(Gallows(0,0))


myapp = Hangman(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
