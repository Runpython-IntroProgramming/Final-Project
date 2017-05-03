
from ggame import App, RectangleAsset, CircleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
black = Color(0, 1)
lgreen = Color(0xd9ffcc, 1.0)
dgreen = Color(0x006600, 1.0)
purp = Color(0x9900cc, 1.0)
blue = Color(0x3399ff,1.0)
gold = Color(0xcc9900, 1.0)
red = Color(0xff6666, 1.0)
noline = LineStyle(0, black)
topr = RectangleAsset (1080, 20, noline, dgreen) 
botr = RectangleAsset (1080, 20, noline, dgreen) 
mtopr = RectangleAsset (300, 20, noline, dgreen) 
mbotr = RectangleAsset (300, 20, noline, dgreen)
sider = RectangleAsset (20, 720, noline, dgreen) 
capr = RectangleAsset (2, 30, noline, dgreen)
player = RectangleAsset (20, 50, noline, purp)
heart = CircleAsset (15, noline, red)
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
        barh.step()
        barj.step()
        bark.step()
        barl.step()
    

class top(Sprite):
    def __init__(self,position):
        super().__init__(topr, position)
        
class mtop(Sprite):
    def __init__(self,position):
        super().__init__(mtopr, position)

class bot(Sprite):
    def __init__(self,position):
        super().__init__(botr, position)
        
class mbot(Sprite):
    def __init__(self,position):
        super().__init__(mbotr, position)

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
    def __init__(self, position, vx, vy, ti, delay):
        super().__init__(barrels, position)
        self.vx = vx
        self.vy = vy
        self.ti = ti
        self.origx = self.x
        self.origy = self.y
        self.onblock=0
        self.go = 0
        self.tim=0
        self.delay = delay
    def start(self):
        self.visible = True
        self.go = 1
        self.x = self.origx
        self.y = self.origy
    def dead(self):
        for x in myapp.getSpritesbyClass(bar):
            x.tim = -2
            x.x = x.origx
            x.y = x.origy
            x.go=0
    def step(self):
        self.tim+=1
        if self.tim == self.delay:
            self.start()
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
            onm = self.collidingWithSprites(mtop)
            if len(on) + len(onm) > 0:
                self.ti = 0
                self.vy = 0
                self.onblock = 1
            if len(on) == 0:
                self.onblock=0
            csides = self.collidingWithSprites(side)
            if len(csides) > 0:
                self.vx=-self.vx
            if self.x > 1030 and self.y>650:
                self.x=540
                self.y=12
            
            

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
        self.dead = 0
        self.countlives = 3
    def step(self):
        self.dead = 0
        self.onblock=0
        if self.wub == 0:
            self.ti=self.ti+0.012
        self.vy =self.ti+self.vy
        self.y=self.y+self.vy
        self.x=self.x+self.vx
        on = self.collidingWithSprites(top)
        onm = self.collidingWithSprites(mtop)
        if len(on) + len(onm) > 0:
            self.ti = 0
            self.vy = 0
            self.y-=.6
            self.onblock = 1
        if len(on) + len(onm) == 0:
            self.onblock = 0
        if self.ti>0.72:
            self.y-=8
        under = self.collidingWithSprites(bot)
        underm = self.collidingWithSprites(mbot)
        if len(under) + len (underm) > 0:
            self.vy=-0.25*self.vy
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
                self.onblock=0
        if self.wub == 1:
            if self.onblock == 1:
                self.vy -= 3.1
                self.ti+=0.0008
                self.wub = 0
        self.onblock=1
        be = self.collidingWithSprites(bar)
        if len(be) >= 1:
            self.x=1000
            self.y=660
            self.ti=2
            be[0].dead()
            if self.countlives == 3:
                hearta.firstloss()
            if self.countlives ==2:
                heartb.secondloss()
            if self.countlives ==1:
                heartc.lastloss()
            if self.countlives ==0:
                play.stop()
            self.countlives -= 1
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
    def stop(self):
        self.vx=0
        self.vy=0
        self.ti=0
        
        
class liv(Sprite):
    def __init__(self, position, lives):
        super().__init__(heart, position)
        self.lives = lives
    def firstloss (self):
        if self.lives == 3:
            self.visible = False
            self.lives = 2
    def secondloss (self):
        if self.lives == 2:
            self.visible = False
            self.lives = 1
    def lastloss (self):
        if self.lives == 1:
            self.visible = False
            self.lives = 0
            
        

myapp = dk(SCREEN_WIDTH, SCREEN_HEIGHT)



leveltwo = [top ((0, 710)), bot ((0, -10)), side ((-10, 0)), side ((1070, 0)),
top ((500, 580)), bot ((500, 590)), cap ((498, 580)), top ((-750, 580)), bot ((-750, 590)), cap ((328, 580)),
top ((750, 450)), bot ((750, 460)), cap ((748, 450)), top ((-900, 450)), bot ((-900, 460)), cap ((178, 450)), mtop ((300, 450)), mbot ((300, 460)), cap ((298, 450)), cap ((600, 450)),
top ((700, 320)), bot ((700, 330)), cap ((698, 320)), top ((-500, 320)), bot ((-500, 330)), cap ((580, 320)),
top ((900, 190)), bot ((900, 200)), cap ((898, 190)), top ((-300, 190)), bot ((-300, 200)), cap ((780, 190))]

playe = play((1000, 640), 0, 0, 0)
prizee = win((300, 175))
prizee = win((540, 10))

bare = bar ((540, 12), 2, 0, 0, 5)
barh = bar ((540, 12), -2, 0, 0, 20)
barj = bar ((540, 12), 1.5, 0, 0, 600)
bark = bar ((540, 12), -2, 0, 0, 1100)
barl = bar ((540, 12), 2, 0, 0, 1200)

hearta = liv ((32, 30), 3)
heartb = liv ((72, 30), 2)
heartc = liv ((112, 30), 1)




    













myapp.run()