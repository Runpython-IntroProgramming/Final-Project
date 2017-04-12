
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
black = Color(0, 1)
lgreen = Color(0xd9ffcc, 1.0)
purp = Color(0x9900cc, 1.0)
blue = Color(0x3399ff,1.0)
noline = LineStyle(0, black)
topr = RectangleAsset (100, 20, noline, lgreen) 

class dk (App):
    def __init__(self, width, height):
            super().__init__(width, height)
            black = Color(0, 1)
            noline = LineStyle(0, black)
            bg_asset = RectangleAsset(width, height, noline, black)
            bg = Sprite(bg_asset, (0,0))
    

class top(Sprite):
    def __init__(self,position):
        super().__init__(topr, position)
    












myapp = dk(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run