
from ggame import App, RectangleAsset, CircleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
black = Color(0, 1)
lgreen = Color(0xd9ffcc, 1.0)
dgreen = Color(0x006600, 1.0)
purp = Color(0x9900cc, 1.0)
blue = Color(0x3399ff,1.0)
gold = Color(0xcc9900, 1.0)
noline = LineStyle(0, black)
topr = RectangleAsset (1080, 20, noline, dgreen) 
botr = RectangleAsset (1080, 20, noline, dgreen) 
sider = RectangleAsset (20, 720, noline, dgreen) 
capr = RectangleAsset (2, 30, noline, dgreen)
player = RectangleAsset (20, 50, noline, purp)
prize = RectangleAsset (35, 15, noline, gold)
barrels = CircleAsset (10, noline, black)
vy=0
vx=0
ti=0

class dk(App):
    def __init__(self, width, height):
            super().__init__(width, height)
            bg_asset = RectangleAsset(width, height, noline, lgreen)
            bg = Sprite(bg_asset, (0,0))
    def step (self):
        playe.step()
        bare.step()
        
    

class top(Sprite):
    def __init__(self,position):
        super().__init__(topr, position)

class bot(Sprite):
    def __init__(self,position):
        super().__init__(botr, position)

class side(Sprite):
    def __init__(self,position):
        super().__init__(sider, position)

class cap(Sprite):
    def __init__(self,position):
        super().__init__(capr, position)
        
class win(Sprite):
    def __init__(self,position):
        super().__init__(prize, position)
   
onblock = 0
jump = 0
wub=0
go = 0

class bar(Sprite):
    def __init__(self, position, vx, vy, ti):
        super().__init__(barrels, position)
        self.vx = vx
        self.vy = vy
        self.ti = ti
        self.onblock=0
        self.go = 0
        self.vx = 2
    def step(self):
        self.go=1
        if self.go == 1:
            if self.onblock == 1:
                self.ti = 0
                self.vy = 0
            self.vy =self.ti+self.vy
            self.y=self.y+self.vy
            self.x=self.x+self.vx
            if onblock != 1:
                self.ti += 0.005
            on = self.collidingWithSprites(top)
            if len(on) > 0:
                self.ti = 0
                self.vy = 0
                self.onblock = 1
            if len(on) == 0:
                self.onblock=0
            csides = self.collidingWithSprites(side)
            ccap = self.collidingWithSprites(cap)
            if len(csides) > 0:
                self.vx=-self.vx
            if len(ccap) > 0:
                self.vx=-self.vx

class play(Sprite):
    def __init__(self, position, vx, vy, ti):
        super().__init__(player, position)
        dk.listenKeyEvent('keydown', 'left arrow', self.lup)
        dk.listenKeyEvent('keydown', 'right arrow', self.rup)
        dk.listenKeyEvent('keydown', 'up arrow', self.uup)
        dk.listenKeyEvent('keydown', 'w', self.wup)
        self.vx=vx
        self.vy=vy
        self.ti=ti
        self.onblock=0
        self.jump = 0
        self.wub =0
    def step(self):
        onblock=0
        if self.wub == 0:
            self.ti=self.ti+0.01
        self.vy =self.ti+self.vy
        self.y=self.y+self.vy
        self.x=self.x+self.vx
        on = self.collidingWithSprites(top)
        if len(on) > 0:
            self.ti = 0
            self.vy = 0
            self.y-=.5
            self.onblock = 1
        under = self.collidingWithSprites(bot)
        if len(under) > 0:
            self.vy=-self.vy
            self.y+=10
        csides = self.collidingWithSprites(side)
        ccap = self.collidingWithSprites(cap)
        if len(csides) > 0:
            self.vx=-self.vx
        if len(ccap) > 0:
            self.vx=-self.vx
        if self.jump == 1:
            if self.onblock ==1:
                self.vy -= 7.5
                self.jump = 0
        if self.wub == 1:
            if self.onblock == 1:
                self.vy -= 3
                self.ti+=0.0012
                self.wub = 0
    def rup(self, event):
        if self.vx<3:
            self.vx+=1
    def lup(self, event):
        if self.vx>-3:
            self.vx-=1
    def uup(self, event):
        if self.onblock==1:
            self.jump = 1
    def wup(self, event):
        self.wub = 1
        
        
        

myapp = dk(SCREEN_WIDTH, SCREEN_HEIGHT)

top ((0, 710))
bot ((0, -10))
side ((-10, 0))
side ((1070, 0))

top ((500, 580))
bot ((500, 590))
cap ((498, 580))
top ((-800, 580))
bot ((-800, 590))

top ((800, 450))
bot ((800, 460))
top ((-400, 450))
bot ((-400, 460))

top ((700, 320))
bot ((700, 330))
top ((-500, 320))
bot ((-500, 330))

top ((900, 190))
bot ((900, 200))
top ((-300, 190))
bot ((-300, 200))

playe = play((1000, 640), 0, 0, 0)
prizee = win((300, 175))
prizee = win((540, 10))

bare = bar ((540, 12), 0, 0, 0)





    













myapp.run()