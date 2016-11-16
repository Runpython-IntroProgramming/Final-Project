"""
by Liam A.
used: http://www.december.com/html/spec/color

"""

from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset
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

class Icon(Sprite):
    def __init__(self,asset,position):
        self.a="no"
        super().__init__(asset, position)
        Draw.listenMouseEvent("mouseup", self.ym_up)
        Draw.listenMouseEvent("mousedown", self.nm_dn)
    def ym_up(self,event):
        self.a="yes"
        self.diffx = self.x-
    def nm_dn(self,event):
        self.a="no"

class Flowr(Icon):
    asset = ImageAsset("images/pinkflowr.png")
    def __init__(self,position):
        super().__init__(Flowr.asset, position)
class Tree(Icon):
    asset = ImageAsset("images/tree.png")
    def __init__(self,position):
        super().__init__(Tree.asset, position)
class Cat(Icon):
    asset = ImageAsset("images/cute-cartoon-cat-cute-light-brown-cartoon-cat-with-a-black-nose-and-7VM6VK-clipart.png")
    def __init__(self,position):
        super().__init__(Cat.asset, position)

class Bunny(Icon):
    asset = ImageAsset("images/bunny.png")
    def __init__(self,position):
        super().__init__(Bunny.asset, position)

"""
while Draw.a="yes"
    diffxcat = acat.x-
    diffxflr 
    diffxbun
    diffxtree
    if aflr.x
"""

class Draw(App):
    def __init__(self, width, height):
        self.a="no"
        super().__init__(width, height)
        abun = Bunny((45, 480))
        abun.scale = 0.8
        acat = Cat((30, 320))
        acat.scale = 0.2
        atree = Tree((45, 160))
        atree.scale = 0.5
        aflr = Flowr((30, 100))
        aflr.scale = 0.1


my_draw = Draw(SCREEN_WIDTH, SCREEN_HEIGHT)
my_draw.run()