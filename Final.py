"""
by Liam A.
used: http://www.december.com/html/spec/color

step functions

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
clkun=[]
clkdx=[]

class Icon(Sprite):
    def __init__(self,asset,position,prop):
        self.a="no"
        self.b=0
        self.c=0
        self.both=False
        chk = 0 #preparing to check a condition
        self.ct = 1 #nothing has been clicked on
        super().__init__(asset, position)
        self.center=(0.5,0.5)
        Draw.listenMouseEvent("mouseup", self.nm_up)
        if prop=True:
            Draw.listenMouseEvent("mousedown", self.ym_dn)

    def ym_dn(self,event):
        self.a="yes"
        lgtha = len(clkun)
        if (self.ct)%2 == 1:
            #calculating whether the mouse is close to an icon:
            self.diffx = self.x-event.x
            self.diffy = self.y-event.y
            self.diffx = abs(self.diffx)
            self.diffy = abs(self.diffy)
            if self.diffx <= 40:
                self.b=2
            else:
                self.b=0
            if self.diffy <= 40:
                self.c=2
            else:
                self.c=0
            if self.c==2 and self.b==2:
                print(type(self), id(self), "first click")
                clkun.append((event.x,event.y)) #add coord. of where clicked...
                clkun.append(type(self)) #and what icon was clicked, to list 'clkun'
                #print("list1: ", list(clkun))
        else:
            chk = clkun[lgtha-1]
            if chk == type(self):
                clkdx.append((event.x,event.y)) #add coord. of where clicked...
                #print("list2: ", list(clkdx))
                lgthb = len(clkdx)
                clkun[lgtha-1](clkdx[lgthb-1], False) #place the selected icon: @ lgth+2, @ clicked location: lgth+1
                #print(clkun[lgtha-1], end=' ')
                #print("!!!THEN!!!", clkdx[lgthb-1])
            
        self.ct += 1
    def nm_up(self,event):
        self.a="no"

class Flowr(Icon):
    asset = ImageAsset("images/pinkflowr.png")
    def __init__(self,position,prop):
        super().__init__(Flowr.asset, position,prop)
        self.scale = 0.1
class Tree(Icon):
    asset = ImageAsset("images/tree.png")
    def __init__(self,position,prop):
        super().__init__(Tree.asset, position,prop)
        self.scale = 0.5
class Cat(Icon):
    asset = ImageAsset("images/cute-cartoon-cat-cute-light-brown-cartoon-cat-with-a-black-nose-and-7VM6VK-clipart.png")
    def __init__(self,position,prop):
        super().__init__(Cat.asset, position,prop)
        self.scale = 0.2
class Bunny(Icon):
    asset = ImageAsset("images/bunny.png")
    def __init__(self,position,prop):
        super().__init__(Bunny.asset, position,prop)
        self.scale = 0.8

class Draw(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        abun = Bunny((65, 520), True)
        acat = Cat((85, 380), True)
        atree = Tree((75, 200), True)
        aflr = Flowr((50, 105), True)
        #bflr = Flowr((650, 420))
    def step(self):
        pass

my_draw = Draw(SCREEN_WIDTH, SCREEN_HEIGHT)
my_draw.run()