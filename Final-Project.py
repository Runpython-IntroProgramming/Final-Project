from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame
from math import floor

blue = Color(0x2EFEC8, 1.0)
black = Color(0x000000, 1.0)
pink = Color(0xFF00FF, 1.0)
red = Color(0xFF5733, 1.0)
orange = Color(0xe66700, 1.0)
white = Color(0xFFFFFF, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x009933, 1.0)
peagreen = Color(0x66ff33, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
grey = Color(0xC0C0C0, 1.0)
brown= Color(0x996633, 1.0)
lightbrown= Color(0xc68c53, 1.0)
lightbrown2= Color(0xac7339, 1.0)
thinline = LineStyle(2, black)
blkline = LineStyle(1, black)
noline = LineStyle(0, white)
coolline = LineStyle(1, grey)
blueline = LineStyle(2, blue)
redline = LineStyle(1, red)
greenline = LineStyle(1, green)
whiteline = LineStyle(1, white)
gridline = LineStyle(1, grey)
tile1 = Color(0x00b33c, 1.0)
tile2 = Color(0x00e64d, 1.0)

# Sunflower---------------------------------------------------------------------

class Sunflower(Sprite):
    def __init__(self,position):
        sunflower_asset = ImageAsset("images/clipart644433 (1).png")
        sh = 100
        super().__init__(sunflower_asset, position)
        self.scale = 0.17
        
class Sun(Sprite):
    def __init__(self,position):
        sun_asset = ImageAsset("images/clipart90644.png")
        self.vy = 1
        super().__init__(sun_asset, position)
        self.scale = 0.03
    
class Sundestroyer(Sprite):
    def __init__(self,position):
        destroyer_asset = CircleAsset(0, noline, black)
        super().__init__(destroyer_asset, position)
        
# Walnut------------------------------------------------------------------------

class Walnut(Sprite):
    def __init__(self,position):
        walnut_asset = ImageAsset("images/kisspng-plants-vs-zombies-2-it-s-about-time-english-waln-walnut-5ab4aed18776e0.5829646215217906735549.png")
        super().__init__(walnut_asset, position)
        self.scale = 0.085
        
# Peashooter--------------------------------------------------------------------

class Peashooter(Sprite):
    def __init__(self,position):
        peashooter_asset = ImageAsset("images/clipart215049.png")
        rph = 7
        super().__init__(peashooter_asset, position)
        self.scale = 0.07
        
class Pea(Sprite):
    def __init__(self,position):
        pea_asset = CircleAsset(13, thinline, peagreen)
        self.vx = 0
        super().__init__(pea_asset, position)
        
# Zombie------------------------------------------------------------------------

class RegularZombie(Sprite):
    def __init__(self,position):
        regularzombie_asset = ImageAsset("images/clipart844194.png")
        self.vx = 0
        self.rzh = 10
        super().__init__(regularzombie_asset, position)
        self.scale = 0.23
        
# Background---------------------------------------------------------------------        

class Background(Sprite):
    def __init__(self,position):
        background = ImageAsset("images/1.jpg")
        super().__init__(background, position)
        self.scale = 1.5

# PvZ---------------------------------------------------------------------------

class PvZ(App):
    def __init__(self,width,height):
        super().__init__(width,height)
        
# House+Background--------------------------------------------------------------
        print("You have " + str(self.Amount_of_Sun) + " of Sun")
        
        Background((0,0))
        
        houseroof = RectangleAsset(200, 325, thinline, lightbrown)
        Sprite(houseroof,(-90,45))
        houseroof2 = RectangleAsset(200, 325, thinline, lightbrown2)
        Sprite(houseroof2,(-90,370))
        
        chimney = RectangleAsset(50, 60, thinline, orange)
        Sprite(chimney,(20,245))
        
        chimneyhole = RectangleAsset(20, 30, thinline, black)
        Sprite(chimneyhole,(35,260))
        
        clx=27
        cly=245
        for a in range (6):
            chimneyline = RectangleAsset(2, 60, noline, black)
            Sprite(chimneyline,(clx,cly))
            clx += 7
        
        clax = 20
        clay = 260
        for a in range (4):
            chimneylineacross = RectangleAsset(50, 2, noline, black)
            Sprite(chimneylineacross,(clax,clay))
            clay += 15
        
# Grid--------------------------------------------------------------------------
        
        grid = RectangleAsset(110,110,whiteline,tile1)
        grid2 = RectangleAsset(110,110,whiteline,tile2)
        
        x = 150 
        y = 125
        for a in range(10):
            Sprite(grid2,(x,y))
            x = x + 110
        
        c = 150 
        d = 110+125
        for a in range(10):
            Sprite(grid,(c,d))
            c = c + 110
         
        e = 150 
        f = 2*(110)+125
        for a in range(10):
            Sprite(grid2,(e,f))
            e = e + 110
         
        g = 150 
        h = 3*(110)+125
        for a in range(10):
            Sprite(grid,(g,h))
            g = g + 110
         
        k = 150 
        l = 4*(110)+125
        for a in range(10):
            Sprite(grid2,(k,l))
            k = k + 110
            
# Function Calling--------------------------------------------------------------
       
        PvZ.listenMouseEvent("mousemove", self.moveMouse)
        PvZ.listenKeyEvent('keydown', 's', self.sunflowerplacement) 
        PvZ.listenKeyEvent('keydown', 'p', self.peashooterplacement) 
        PvZ.listenKeyEvent('keydown', 'w', self.walnutplacement)
        PvZ.listenMouseEvent('click', self.sundestroyerplacement)
        
# Functions---------------------------------------------------------------------
       
        x=0
        y=0
        
    def moveMouse(self, event):
            self.x = event.x
            self.y = event.y
    
    def sunflowerplacement(self,event):
        if self.Amount_of_Sun >= 50:
            x = (floor(self.x/110)*110) + 52
            y = (floor(self.y/110)*110) + 20
            if x >= 150 and x <= 1248 and y >= 125 and y <= 675:
                Sunflower((x,y))
                self.Amount_of_Sun -= 50
                print("You have " + str(self.Amount_of_Sun) + " of Sun")
                    
                
    
    def peashooterplacement(self,event):
        if self.Amount_of_Sun >= 100:
            x = (floor(self.x/110)*110) + 52
            y = (floor(self.y/110)*110) + 25
            if x >= 150 and x <= 1248 and y >= 125 and y <= 675:
                Peashooter((x,y))
                self.Amount_of_Sun -= 100
                print("You have " + str(self.Amount_of_Sun) + " of Sun") 
        
    def walnutplacement(self,event):
        if self.Amount_of_Sun >= 100:
            x = (floor(self.x/110)*110) + 55
            y = (floor(self.y/110)*110) + 25
            if x >= 150 and x <= 1248 and y >= 125 and y <= 675:
                Walnut((x,y))
                self.Amount_of_Sun -= 50
                print("You have " + str(self.Amount_of_Sun) + " of Sun") 
    
    def sundestroyerplacement(self,event):
        Sundestroyer((self.x,self.y))

        
 
# Step--------------------------------------------------------------------------
    time = 0  
    Amount_of_Sun = 50
    def step(self):
        self.time += 1
        #print(self.time)
        if self.time > 0:
            
            for a in self.getSpritesbyClass(Pea):
                a.x += a.vx
                a.vx = 5
                if a.x >= 1800:
                    a.destroy()
            
                else:    
                    for b in self.getSpritesbyClass(RegularZombie):
                        if a.collidingWith(b):
                            b.rzh -= 1
                            if b.rzh >= 0:
                                a.destroy()
                                
            for a in self.getSpritesbyClass(Sun):
                a.y += a.vy
                if a.y >= 800:
                    a.destroy()
                
                for b in self.getSpritesbyClass(Sundestroyer):
                    if b.collidingWith(a) == False:
                        b.destroy()
                        
                    elif b.collidingWith(a):
                        a.destroy()
                        b.destroy()
                        self.Amount_of_Sun += 50
                        print("You have " + str(self.Amount_of_Sun) + " of Sun") 
                    
            for a in self.getSpritesbyClass(RegularZombie):
                a.x -= a.vx
                a.vx = 0.4
            
                if a.collidingWithSprites(Pea):
                    a.rzh -= 1
                    if a.rzh <= 0:
                        a.destroy()
            
            for a in self.getSpritesbyClass(Peashooter):
                if self.time % 100 == 0:
                    Pea((a.x+70,a.y+15))
            
            for a in self.getSpritesbyClass(Sunflower):
                x = a.x
                y = a.y
                if self.time % 800 == 0:
                    sun = Sun((x,y))
                    sun.vy = -0.2
                    
            for a in self.getSpritesbyClass(Peashooter):
                for b in self.getSpritesbyClass(RegularZombie): 
                    if b.collidingWith(a):
                        b.vx = 0
                        if time % 200 == 0:
                            a.rph - 1
                    
# Natural Sun-------------------------------------------------------------------

            x = 300
            y = -100
            if self.time == 200:
                Sun((x,y))
                
            if self.time == 500:
                Sun((x+300,y))
                
            if self.time == 1000:
                Sun((x+600,y))
                
            if self.time == 1500:
                Sun((x+300,y))
                
            if self.time == 2500:
                Sun((x+600,y))
                
            if self.time == 3500:
                Sun((x,y))
               
# Zombies-----------------------------------------------------------------------
            #Lane 1 = RegularZombie((x, y - 30))
            #Lane 2 = RegularZombie((x, y + 80))
            #Lane 3 = RegularZombie((x, y + 190))
            #Lane 4 = RegularZombie((x, y + 300))
            #Lane 5 = RegularZombie((x, y + 410))
            
            x = 1250
            y = 125
            
            if self.time == 400:
                RegularZombie((x, y - 30))
                
            if self.time == 900:
                RegularZombie((x, y + 300))
                
            if self.time == 1800:
                RegularZombie((x, y + 410))
                
            if self.time == 2200:
                RegularZombie((x, y + 80))
            
            if self.time == 2500:
                RegularZombie((x, y + 190))
                
            if self.time == 2600:
                RegularZombie((x, y - 30))    
                   
myapp = PvZ(1270,720)
myapp.run()