"""
Creator: Peter Bynum
Sources:

"""

from random import randint
from ggame import App, Color, LineStyle, Sprite, CircleAsset, RectangleAsset, EllipseAsset, PolygonAsset, TextAsset

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 300

difficulty = input("Please choose a difficulty level: easy, medium, or hard")

easywords = ['monkey', 'breeze', 'cookies', 'vapor', 'shallow']
mediumwords = [
hardwords = [

class Hangman(App):
    def __init__(self, width, height):
        super().__init__(width, height)



myapp = Hangman(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()