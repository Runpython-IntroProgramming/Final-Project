"""
by Liam A.
used: http://www.december.com/html/spec/color

step functions

"""

from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800

# Colors
Lgreen = Color (0x7CFC00, 0.95)
turqo = Color (0x40E0D0, 0.99)
orange = Color (0xFF8600, 1)
black = Color (0x000000, 0.85)
purp = Color (0x68228B, 0.6)
brn = Color (0x5C3317, 0.9)
pale = Color (0xFFFACD, 0.4)
white = Color (0xFFFFFF, 0)

bl_line = LineStyle(3, black)
thinline = LineStyle(1, black)
noline = LineStyle(0, white)

clkun=[]
clkdx=[]
stage=1
color=0
dotg = CircleAsset(1, noline, Lgreen)
dotq = CircleAsset(1, noline, turqo)
doto = CircleAsset(1, noline, orange)
dotb = CircleAsset(1, noline, black)
dotp = CircleAsset(1, noline, purp)
dotr = CircleAsset(1, noline, brn)
dotl = CircleAsset(1, noline, pale)
box = RectangleAsset(10, 100, thinline, black)

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
        if prop==True:
            Draw.listenMouseEvent("mousedown", self.ym_dn)

    def ym_dn(self,event):
        self.a="yes"
        global stage
        lgtha = len(clkun)
        if stage == 1:
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
            else:
                chk = clkun[lgtha-1]
                if chk == type(self):
                    clkdx.append((event.x,event.y)) #add coord. of where clicked...
                    lgthb = len(clkdx)
                    clkun[lgtha-1](clkdx[lgthb-1], False) #place the selected icon: @ lgth+2, @ clicked location: lgth+1
                    #print(clkun[lgtha-1], end=' ')
                    #print(clkdx[lgthb-1])
        self.ct += 1

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
    #global stage
    #global color
    def __init__(self, width, height):
        global stage
        super().__init__(width, height)
        self.a=0
        abun = Bunny((65, 520), True)
        acat = Cat((85, 380), True)
        atree = Tree((75, 200), True)
        aflr = Flowr((50, 105), True)
        #bflr = Flowr((650, 420))
        Sprite(box, (80, 10))
        Draw.listenKeyEvent("keydown", "enter", self.switch)
        if stage == 2:
            Draw.listenKeyEvent("keydown", "g", self.green)
            Draw.listenKeyEvent("keydown", "q", self.turq)
            Draw.listenKeyEvent("keydown", "o", self.orange)
            Draw.listenKeyEvent("keydown", "b", self.black)
            Draw.listenKeyEvent("keydown", "p", self.purp)
            Draw.listenKeyEvent("keydown", "r", self.brn)
            Draw.listenKeyEvent("keydown", "l", self.pale)
            Draw.listenMouseEvent("mousedown", self.mse_isdn)
            Draw.listenMouseEvent("mouseup", self.mseno)
    def switch(self,event):
        global stage
        stage += 1
        print("news! ", stage)
    def mse_isdn(self,event):
        self.a=1
        self.mse_x = event.x
        self.mse_x = event.y
    def mseno(self,event):
        self.a=0
    def green(self,event):
        global color
        color = 1
    def turq(self,event):
        global color
        color = 2
    def orange(self,event):
        global color
        color = 3
    def black(self,event):
        global color
        color = 4
    def purp(self,event):
        global color
        color = 5
    def brn(self,event):
        global color
        color = 6
    def pale(self,event):
        global color
        color = 7
    def step(self):
        global color
        if self.a == 1 and color != 0:
            print ("go colors go")
            if color == 1:
                Sprite(dotg, (self.mse_x,self.mse_y))
            if color == 2:
                Sprite(dotq, (self.mse_x,self.mse_y))
            if color == 3:
                Sprite(doto, (self.mse_x,self.mse_y))
            if color == 4:
                Sprite(dotb, (self.mse_x,self.mse_y))
            if color == 5:
                Sprite(dotp, (self.mse_x,self.mse_y))
            if color == 6:
                Sprite(dotr, (self.mse_x,self.mse_y))
            if color == 7:
                Sprite(dotl, (self.mse_x,self.mse_y))
    #"""
    

my_draw = Draw(SCREEN_WIDTH, SCREEN_HEIGHT)
my_draw.run()