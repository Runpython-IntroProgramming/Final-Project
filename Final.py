"""
by Liam A.
used: http://www.december.com/html/spec/color

how to change location to center?
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
est=[]
ct = 0 #nothing has been clicked on

class Icon(Sprite):
    def __init__(self,asset,position):
        self.a="no"
        self.b=0
        self.c=0
        self.both=False
        self.ch=0
        self.L_c=0
        self.L_d=0
        super().__init__(asset, position)
        self.center=(0.5,0.5)
        Draw.listenMouseEvent("mouseup", self.nm_up)
        Draw.listenMouseEvent("mousedown", self.ym_dn)
    def ym_dn(self,event):
        global ct
        self.a="yes"
        lgth = len(est)
        if self.ch==1:
            #print(lgth) #length of 'est'
            pass
        if ct%2 == 0:
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
            print(self.b)
            print(self.c)
            print("_____________")
            if self.c==2 and self.b==2:
                print(type(self), id(self))
                est.append(((event.x,event.y),"retrieve")) #add coord. of where clicked...
                est.append(type(self)) #and what icon was clicked, to list 'est'
                print(list(est))
                self.ch=1
            else:
                self.ch=0 #entries have not been added to list 'est'
        else:
            est.append((event.x,event.y)) #add coord. of where clicked...
            est.append(est[lgth-1]) #and what icon was clicked, to list 'est'
            print(list(est))
            self.ch=0
            self.L_c=lgth
            self.L_d=lgth+1
            est[self.L_d](est[self.L_c]) #place the selected icon: @ lgth+2, @ clicked location: lgth+1
            print(est[self.L_d], end=' ')
            print(est[self.L_c])
        ct += 1
    def nm_up(self,event):
        self.a="no"

class Flowr(Icon):
    asset = ImageAsset("images/pinkflowr.png")
    def __init__(self,position):
        super().__init__(Flowr.asset, position)
        self.scale = 0.1
class Tree(Icon):
    asset = ImageAsset("images/tree.png")
    def __init__(self,position):
        super().__init__(Tree.asset, position)
        self.scale = 0.5
class Cat(Icon):
    asset = ImageAsset("images/cute-cartoon-cat-cute-light-brown-cartoon-cat-with-a-black-nose-and-7VM6VK-clipart.png")
    def __init__(self,position):
        super().__init__(Cat.asset, position)
        self.scale = 0.2
class Bunny(Icon):
    asset = ImageAsset("images/bunny.png")
    def __init__(self,position):
        super().__init__(Bunny.asset, position)
        self.scale = 0.8
class Draw(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        abun = Bunny((65, 520))
        #abun.scale = 0.8
        acat = Cat((85, 380))
        #acat.scale = 0.2
        atree = Tree((75, 200))
        #atree.scale = 0.5
        self.aflr = Flowr((50, 105))
        #self.aflr.scale = 0.1
        #self.bflr = Flowr((650, 420))
    def step(self):
        pass

my_draw = Draw(SCREEN_WIDTH, SCREEN_HEIGHT)
my_draw.run()