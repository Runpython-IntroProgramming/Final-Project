"""
by Liam A.
used: http://www.december.com/html/spec/color

"""

from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

# Colors
Lgreen = Color (0x7CFC00, 0.95)
turqo = Color (0x40E0D0, 0.99)
Orange = Color (0xFF8600, 1)
black = Color (0x000000, 0.85)
purp = Color (0x68228B, 0.6)
brn = Color (0x5C3317, 0.9)
pale = Color (0xFFFACD, 0.4)

bl_line = LineStyle(3, black)
thinline = LineStyle(1, black)

class Flowr(Sprite):
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
    def _init_
        position(30, 100)
class Tree(Sprite):
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
    def _init_
        position(45, 160)
class Cat(Sprite):
    asset = ImageAsset("images/cute-cartoon-cat-cute-light-brown-cartoon-cat-with-a-black-nose-and-7VM6VK-clipart.png",
    def _init_
        position(30, 220)

class Cat(Sprite):
    asset = ImageAsset("images/bunny.png",
    def _init_
        position(30, 220)


class Draw(App):
    SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)

my_draw = App()
my_draw.run()