"""
platformer.py
Author:waSclthu11
Credit:The example platformer program helped a lot, especially with subclasses, which I used for the terrain. Also Mr.Dennison helped with the collision detection setup.
Sprite credit link: https://goglilol.itch.io/cute-knight
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
#grid=lambda W: (W-W%51)
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, TextAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame
x=510
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
blue = Color(0x0000FF, 1.0)
black = Color(0x000000, 1.0)
pink = Color(0xFF00FF, 1.0)
red = Color(0xFF5733, 1.0)
white = Color(0xFFFFFF, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
brown = Color(0x8B4513, 1.0) #8B4513
purple = Color(0x800080, 1.0)
white = Color(0xffffff, 1.0)
grey = Color(0xC0C0C0, 1.0)

thinline = LineStyle(2, black)
blkline = LineStyle(1, black)
noline = LineStyle(0, white)
coolline = LineStyle(1, grey)
blueline = LineStyle(2, blue)
redline = LineStyle(1, red)
greenline = LineStyle(1, green)
gridline = LineStyle(1, grey)
grid=RectangleAsset(30,30,gridline,white)


from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

class Player(Sprite):
    asset = ImageAsset("images/SpriteFinalproj1.png", Frame(0,36,64,28), 8, 'horizontal')
    asset.append("images/sheet_hero_walk.png", Frame(0,36,64,28), 3, 'horizontal')
    asset.append("images/sheet_hero_jump.png", Frame(0,26,64,38), 5, 'horizontal')
    asset.append("images/sheet_hero_stab.png", Frame(0,34,64,30), 5, 'horizontal')
    
    def __init__(self, position,n):
        super().__init__(Player.asset, position, CircleAsset(10))
        self.vx = 0
        self.vy = 0
        self.thrust = 0
        self.left=0
        self.right=0
        self.collidingwithsprites=0
        self.resting=0
        self.collidetop=Collide(position,12,5,green)
        self.collidebottom=Collide(position,8,5,blue)
        self.collideleft=Collide(position,5,15,red)
        self.collideright=Collide(position,5,15,pink)
        self.leftslide=False
        self.stabhit=Collide(position,50,5,brown)
        self.rightslide=False
        self.leftleap=False
        self.rightleap=False
        self.leap=False
        self.attack=False
        self.attackp=True
        self.thrustframe=1
        self.width=64
        self.Attacking=False
        self.Attackcount=0
        if n==0:
            SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
            SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
            SpaceGame.listenKeyEvent("keydown", "left arrow", self.lefton)
            SpaceGame.listenKeyEvent("keyup", "left arrow", self.leftoff)
            SpaceGame.listenKeyEvent("keydown", "right arrow", self.righton)
            SpaceGame.listenKeyEvent("keyup", "right arrow", self.rightoff)
            SpaceGame.listenKeyEvent("keydown", "down arrow", self.Leap)
            SpaceGame.listenKeyEvent("keyup", "down arrow", self.noLeap)
            SpaceGame.listenKeyEvent("keydown", "m", self.Attack)
            SpaceGame.listenKeyEvent("keyup", "m", self.noAttack)
        if n==1:
            SpaceGame.listenKeyEvent("keydown", "w", self.thrustOn)
            SpaceGame.listenKeyEvent("keyup", "w", self.thrustOff)
            SpaceGame.listenKeyEvent("keydown", "a", self.lefton)
            SpaceGame.listenKeyEvent("keyup", "a", self.leftoff)
            SpaceGame.listenKeyEvent("keydown", "d", self.righton)
            SpaceGame.listenKeyEvent("keyup", "d", self.rightoff)
            SpaceGame.listenKeyEvent("keydown", "s", self.Leap)
            SpaceGame.listenKeyEvent("keyup", "s", self.noLeap)
            SpaceGame.listenKeyEvent("keydown", "c", self.Attack)
            SpaceGame.listenKeyEvent("keyup", "c", self.noAttack)
        self.fxcenter = self.fycenter = 0.5
    def step(self):
        downcollide=self.collidebottom.collidingWithSprites(Variblock)
        if self.Attacking==False:
            self.stabhit.x=0
            self.stabhit.y=0
        #Jump Animation
        if not len(downcollide):
            if self.thrustframe<12:
                self.thrustframe=12
            self.setImage(self.thrustframe)
            self.thrustframe += .25
            if self.thrustframe==16:
                self.thrustframe=14  
        #Attack Animation
        elif self.attack==True and self.vy==0 and self.Attackcount==0:
            self.attackp=False
            if self.thrustframe<16.5:
                self.thrustframe=16.5
            self.setImage(self.thrustframe)
            if self.thrustframe==17:
                self.Attacking=True
            self.thrustframe += .125
            if self.thrustframe>=22:
                self.thrustframe=16.5
                self.attackp=False

        #Running Animation
        elif (self.left==1 or self.right==1) and self.vy==0:
            if self.thrustframe<9 or self.thrustframe>11:
                self.thrustframe=9
            """if self.left==1:
                self.width=-64
                print(self.width)
            if self.right==1:
                self.width=64"""
            self.setImage(self.thrustframe)
            self.thrustframe += .25 
            if self.thrustframe == 11:
                self.thrustframe = 9
        #Idle Animation
        elif self.vx==0 and self.resting==1:
            self.setImage(self.thrustframe)
            self.thrustframe += .25
            if self.thrustframe >= 8:
                self.thrustframe = 1

        self.x += self.vx
        self.y += self.vy
        self.collidetop.x = self.x
        self.collidetop.y = self.y-13
        self.collidebottom.x =self.x
        self.collidebottom.y =self.y+12
        self.collideright.x =self.x+7
        self.collideright.y =self.y-1
        self.collideleft.x =self.x-7
        self.collideleft.y =self.y-1
        if self.Attacking==True and self.Attackcount<=20:
            self.stabhit.x=self.x+20
            self.stabhit.y=self.y+5
            self.Attackcount+=1
        elif self.Attackcount>=20:
            self.Attackcount=0
            self.Attacking=False
        upcollide=self.collidetop.collidingWithSprites(Variblock)
        downcollide=self.collidebottom.collidingWithSprites(Variblock)
        downcollidep=self.collidebottom.collidingWithSprites(Platform)
        downcollide.extend(downcollidep)
        downcollides=self.collidebottom.collidingWithSprites(sprong)
        if len(downcollides):
            self.vy=-15
        if len(downcollide):
             if self.vy>0:
                if self.vy>=3:
                    self.y=self.y-self.vy*0.3
                    self.vy=0
                    
                self.vy=0
                self.resting=1
        elif len(downcollide)==0:
            if self.rightslide==True and self.vy>1:
                self.vy=1
                self.leftleap=True
            if self.leftslide==True and self.vy>1:
                self.rightleap=True
                self.vy=1
            else:
                if self.vy<6:
                    self.vy=self.vy+.3
            self.resting=0
            if len(upcollide):
                self.y=self.y+3
                self.vy=self.vy*-.5
            
                
        leftcollide=self.collideleft.collidingWithSprites(Variblock)
        if len(leftcollide):
            #print("left")
            self.x=self.x-self.vx
            self.vx=0
        self.leftslide=True
        if not len(leftcollide):
            self.leftslide=False
            self.rightleap=False
        rightcollide=self.collideright.collidingWithSprites(Variblock)
        if len(rightcollide):
            #print("right")
            self.x=self.x-self.vx
            self.vx=0
            self.rightslide=True
        if not len(rightcollide):
            self.rightslide=False
            self.leftleap=False
        if self.left==1:
            if self.vx>0 and len(downcollide):
                self.vx=0
            if self.vx>=-4:
                self.vx=self.vx-.4
        else:
            if self.right==1:
                if self.vx<0 and len(downcollide):
                    self.vx=0
                if self.vx<=4:
                    self.vx=self.vx+.4
            else:
                if self.resting==1:
                    self.vx=0
        
        if self.thrust == 1:
            self.vy = -6
            self.thrust=0
        else:
            if self.y>=x:
                self.vy=0
        if self.leap==True:
            if self.rightleap==True:
                self.vx=6.5
                self.vy=-5
            if self.leftleap==True:
                self.vx=-6.5
                self.vy=-5
    def thrustOn(self, event):
        if self.resting==1:
            self.thrust = 1
    def thrustOff(self, event):
        self.thrust = 0
    def lefton(self, event):
        self.left=1
    def leftoff(self, event):
        self.left=0
    def righton(self, event):
        self.right=1
    def rightoff(self, event):
        self.right=0
    def Leap(self, event):
        self.leap=True
    def noLeap(self, event):
        self.leap=False
    def Attack(self, event):
        if self.attackp==True:
            self.attack=True
        else:
            self.attack==False
    def noAttack(self, event):
        self.attack=False
        self.attackp=True
class Snake(Sprite):
    asset = ImageAsset("images/sheet_snake_walk.png", Frame(0,40,64,24), 7, 'horizontal')
    asset.append("images/sheet_snake_hurt.png", Frame(0,40,64,24), 2, 'horizontal')
    def __init__(self,position):
        super().__init__(Snake.asset,position, CircleAsset(15))
        self.vx=-1
        self.thrustframe=1
        self.rightdetect=Collide(position,5,15,green)
        self.leftdetect=Collide(position,5,15,red)
        #self.bottomdetect=Collide(position,5,15,blue)
        self.fxcenter = self.fycenter = 0.5
    def step(self):
        self.x += self.vx
        self.rightdetect.x=self.x+10
        self.rightdetect.y=self.y
        self.leftdetect.x=self.x-10
        self.leftdetect.y=self.y
        leftdetect=self.leftdetect.collidingWithSprites(Spike)
        #rightdetect=self.rightdetect.collidingWithSprites(Spike)
        ros=(self.rightdetect.collidingWithSprites(Collide))
        #rightdetect.extend(ros)
        #if len(rightdetect):
        #self.thrustframe+=.25
        if len(leftdetect) or len(ros):
            if self.thrustframe<=7:
                self.thrustframe=8
            self.vx=0
            self.setImage(self.thrustframe)
        else: 
            if self.thrustframe>=7:
                self.thrustframe=1
        self.setImage(self.thrustframe)
        self.thrustframe+=.25
        if self.thrustframe>=9:
            Snake.destroy(self.rightdetect)
            Snake.destroy(self.leftdetect)
            Snake.destroy(self)
class Snakebox(Sprite):
    asset=RectangleAsset(30,30,noline,brown)
    def __init__(self,x,y):
        self.fxcenter = .5
        self.fycenter=.5
        self.Snake1=None
        self.Snake2=None
        self.SnakeSpawn=50
        super().__init__(Snakebox.asset, (x,y))
    def step(self): 
        if self.SnakeSpawn==100:
            #self.Snake1=Snake((self.x, self.y-10))
            self.SnakeSpawn=0
        self.SnakeSpawn+=.5
            
        
class Collide(Sprite):
    def __init__(self, position,w,h,color):
        super().__init__(RectangleAsset(w,h,noline, color), position)
        self.fxcenter = 0.5
        self.fycenter = 0.5
        self.visible=True
class Hitbox(Collide):
    def __init__(self, position,w,h,color):
        super().__init__(RectangleAsset(w,h,noline, color), position)
class Wallblock(Sprite):
    def __init__(self, x, y, w, h, color):
        super().__init__(RectangleAsset(w-1,h-1,noline, color),
            (x, y))
        collideswith = self.collidingWithSprites(type(self))
        if len(collideswith):
            collideswith[0].destroy()
        Wallblock.fxcenter = Wallblock.fycenter = 0
class Platform(Sprite):
    def __init__(self, x, y,m,d):
        self.dcount=0
        self.move=m
        self.d=d
        self.vx=self.d
        super().__init__(RectangleAsset(50, 10, noline,blue),(x,y))
    def step(self):
        if self.move==True:
            self.x+=self.vx
            self.dcount+=1
            if self.dcount>=abs(self.d)*60:
                self.vx=-1*self.vx
                self.dcount=0
class Block(Wallblock):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50, red)

class Variblock(Sprite):
    def __init__(self, w, h, x, y):
        grid=lambda W: (W-W%10)
        gred=lambda W: (W*10)
        super().__init__(RectangleAsset(gred(w),gred(h),noline,grey),(grid(x),grid(y)))

class sprong(Wallblock):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 10, pink)
class goal(Sprite):
    def __init__(self, w, h, x, y):
        super().__init__(RectangleAsset(w,h,noline,blue),(x,y))
class goal2(Sprite):
    def __init__(self, w, h, x, y):
        super().__init__(RectangleAsset(w,h,noline,purple),(x,y))
class Spike(Sprite):
     def __init__(self, w, h, x, y):
        grid=lambda W: (W-W%10)
        gred=lambda W: (W*10)
        super().__init__(RectangleAsset(gred(w),gred(h),noline,red),(grid(x),grid(y)))
class textbox(Sprite):
    def __init__(self, t, s, w, x, y):
        super().__init__(TextAsset(t, style=s, width=w, fill=blue),(x,y))
class SpaceGame(App):
    def __init__(self):
        super().__init__()
        # Background
        x=510
        beeg=50
        black = Color(0, 1)
        noline = LineStyle(0, black)
        TA= TextAsset("Press Enter to Begin", style="bold 40pt Arial", width=250, fill=black)
        self.Enter=Sprite(TA,(400,200))
        self.levelindex=-.5
        self.listenMouseEvent("mousemove", self.Mouse)
        self.listenMouseEvent("click", self.Click)
        self.listenKeyEvent("keydown", "enter", self.newlevel)
        self.listenKeyEvent("keydown", "z", self.uplevel)
        self.listenKeyEvent("keydown", "x", self.downlevel)
        self.levelfinish=[]
        self.terrainlist=None
        self.p = None
        self.c=None
        self.progress=False
    def Click(self, event):
        if self.c:
            self.c.destroy()
        print("hah you're attempt is futile.")
        self.c=Collide(self.pos,5,5,red)
    def Mouse(self, event):
        self.pos = (event.x, event.y)
    def uplevel(self, event):
        self.levelindex+=0.5
    def downlevel(self, event):
        self.levelindex-=0.5
    def newlevel(self,event):
        for s in self.getSpritesbyClass(Player):
            s.destroy()
        for s in self.getSpritesbyClass(Spike):
            s.destroy()
        for a in self.getSpritesbyClass(Variblock):
            a.destroy()
        for c in self.getSpritesbyClass(Collide):
            c.destroy()
        for s in self.getSpritesbyClass(sprong):
            s.destroy()
        for s in self.getSpritesbyClass(textbox):
            s.destroy()
        for s in self.getSpritesbyClass(goal):
            s.destroy()
        for s in self.getSpritesbyClass(Snake):
            s.destroy()
        for s in self.getSpritesbyClass(Snakebox):
            s.destroy()
        for s in self.getSpritesbyClass(Platform):
            s.destroy()
        if self.Enter:
            self.Enter.destroy()
            self.Enter=None
        if self.levelindex==-1:
            self.progress=True
            Variblock(103,52,0,0)
            textbox("<Credits>","bold 40pt Arial",600,320,220)
        if self.levelindex==-.5:
            self.progress=True
            self.p=Player((500,100),0)
            Variblock(103,8,0,0)
            Variblock(103,8,0,435)
            Variblock(8,35,0,80)
            Variblock(8,35,940,80)
            Variblock(50,20,260,160)
            textbox("<Game_Name>","bold 40pt Arial",600,320,220)
            textbox("Start","bold 30pt Arial",200,100,450)
            textbox("Credits","bold 30pt Arial",200,800,450)
            goal(100,20,100,420)
            self.c=goal2(100,20,450,350)
            Spike(10,2,820,420)
        if self.levelindex==0:
            self.progress=True
            self.p=Player((60,350),0)
            Variblock(105,30,0,0)
            Variblock(105,12,0,420)
            Spike(1,12,0,300)
            goal(20,120,1000,300)
            textbox("Press 'Enter' when touching the blue goal to complete the level. The red 'Spikes' will send you back.","bold 40pt Arial",1000,10,10)
        if self.levelindex==0.5:
            self.progress=True
            self.p = Player((60,50),0)
            Variblock(3,105,0,0)
            Variblock(105,4,0,480)
            Variblock(3,90,990,0)
            textbox("Press 'Spacebar' to jump and 'm' to attack","bold 40pt Arial",1000,100,10)
            Variblock(4,8,200,420)
            Variblock(4,8,620,420)
            Snakebox(530,480)
            Spike(1,3,230,450)
            goal(20,20,800,430)
        if self.levelindex==1:
            self.progress=True
            self.p = Player((60,50),0)
            Variblock(5,105,0,0)
            Variblock(105,4,0,480)
            Variblock(39,90,650,0)
            ###NonborderTerrain
            Variblock(21,13,50,150)
            Variblock(9,3,400,150)
            Variblock(3,12,400,150)
            Spike(14,1,260,250)
            Spike(1,9,430,180)
            textbox("You can slide on walls by holding a direction into the wall.","bold 20pt Arial",1000,10,10)
            textbox("And you can jump off the wall by pressing the down arrow.","bold 20pt Arial",380,650,250)
            Spike(21,1,440,400)
            goal(20,20,500,470)
        if self.levelindex==1.5 or self.levelindex==2.5 or self.levelindex==3.5:
            self.progress=True
            self.p=Player((60,350),0)
            Variblock(105,30,0,0)
            Variblock(105,12,0,420)
            Spike(1,12,0,300)
            goal(20,120,1000,300)
        if self.levelindex==4.5:
            self.progress=True
            self.p=Player((60,350),0)
            Variblock(105,30,0,0)
            Variblock(105,12,0,420)
            Spike(1,12,0,300)
            goal(20,120,1000,300)
            textbox("Here's a tough section. Good Luck!","bolf 40pt Arial",1000,500,10)
        if self.levelindex==2:
            self.progress=True
            self.p = Player((60,50),0)
            Variblock(3,105,0,0)
            Variblock(105,4,0,480)
            Variblock(3,90,990,0)
            Variblock(10,30,400,250)
            Spike(10,1,400,250)
            sprong(340,470)
            textbox("This is a spring. It will send you high into the air.","bold 30pt Arial",1000,50,100)
            goal(20,20,510,450)
        if self.levelindex==3:
            self.progress=True
            self.p = Player((100,400),0)
            Variblock(3,105,0,0)
            Variblock(105,4,0,480)
            Variblock(3,90,990,0)
            Variblock(4,10,200,400)
            Variblock(4,14,620,370)
            Platform(570,420,False,0)
            Snakebox(530,480)
            Spike(1,3,230,450)
            goal(20,20,800,440)
        if self.levelindex==4:
            Variblock(3,105,0,0)
            Variblock(105,4,0,500)
            Variblock(3,90,990,0)
            ###Nonborder
            self.p=Player((170,150),0)
            #Level1
            Variblock(50,2,0,400)
            Snakebox(470,500)
            Spike(1,8,30,420)
            Variblock(10,2,800,400)
            Spike(2,2,840,370)
            Variblock(10,2,600,400)
            Spike(2,2,640,370)
            Platform(300,300,True,1)
            Platform(200,300,True,-1)
            Snakebox(470,400)
            Spike(1,18,30,220)
            Variblock(2,10,50,260)
            #Level2
            Variblock(50,2,500,300)
            Platform(500,200,True,2.5)
            #Level3
            Variblock(50,2,0,200)
            Snakebox(470,200)
            Spike(1,18,30,20)
            Variblock(2,10,50,50)
            Platform(50,150,False,0)
            Variblock(5,2,250,70)
            Variblock(5,2,500,70)
            #level4
            Variblock(45,2,550,100)
            Spike(20,1,550,90)
            goal(10,100,980,0)
            ###Snakes!!
        if self.levelindex==5:
            self.progress=True
            self.p = Player((60,50),0)
            Variblock(3,105,0,0)
            Variblock(105,4,0,500)
            Variblock(3,90,990,0)
            ###NonborderTerrain
            Variblock(20,3,30,150)
            Spike(20,1,30,145)
            
            Variblock(3,10,260,210)
            Spike(3,1,260,205)
            #Block 1
            Variblock(80,3,50,410)
            Spike(80,1,50,400)
            #Block 2
            Variblock(10,3,420,280)
            Spike(10,1,420,310)
            Spike(1,3,420,280)
            #Block 3
            Variblock(3,10,600,180)
            Spike(1,10,630,175)
            Spike(3,1,600,175)
            #Block 4
            Variblock(13,3,400,180)
            Variblock(3,10,400,90)
            Spike(13,1,400,200)
            Spike(1,12,400,90)
            #Block 5
            Variblock(10,3,700,300)
            goal(20,20,500,470)
        if self.levelindex==5.5:
            self.p=Player((500,50),0)
            Variblock(3,105,0,0)
            Variblock(3,90,990,0)
            Variblock(105,4,0,500)
            Spike(92,1,30,440)
            goal(100,20,450,500)
            #Walljumps n Stuff
            Variblock(2,15,550,0)
            #Diagonal Jump
            Spike(10,1,450,150)
            Variblock(2,5,430,0)
            Spike(5,1,400,110)
            Spike(5,1,400,50)
            
            Spike(2,1,380,120)
            Spike(2,1,380,60)
            
            Spike(2,1,360,130)
            Spike(2,1,360,70)
            
            sprong(30,430)
            Variblock(6,2,150,100)
            
            Variblock(2,2,450,400)
            Variblock(2,2,550,400)
            Variblock(2,2,620,380)
            
            Variblock(2,5,700,270)
            Spike(2,1,700,260)
            Variblock(2,5,600,230)
            Spike(2,1,600,220)
            sprong(750,300)
            Spike(1,40,800,50)
            Variblock(5,2,800,50)
            Spike(7,1,920,250)
            Variblock(1,5,810,200)
        if self.levelindex==6:
            self.p=Player((50,260),0)
            Variblock(103,20,0,300)
            Variblock(103,25,0,0)
            Snakebox(800,300)
            Snakebox(200,300)
            Snakebox(500,300)
            goal(20,50,1000,250)
    def step(self):
        if self.p:
            self.levelfinish=self.p.collidingWithSprites(goal)
            self.playerhurt=self.p.collidingWithSprites(Spike)
            self.playerhurt1=self.p.collidingWithSprites(Snake)
            self.playerhurt.extend(self.playerhurt1)
            self.select=self.p.collidingWithSprites(goal2)
            if len(self.select):
                self.levelindex=((self.c.x)-self.c.x%100)/100
            if len(self.levelfinish):
                if self.progress==True:
                    print(self.levelindex)
                    self.levelindex=self.levelindex+.5
                    print(self.levelindex)
                    self.progress=False
            if len(self.playerhurt):
                for s in self.getSpritesbyClass(Player):
                    s.destroy()
                for q in self.getSpritesbyClass(Spike):
                    q.destroy()
                for a in self.getSpritesbyClass(Variblock):
                    a.destroy()
                for c in self.getSpritesbyClass(Collide):
                    c.destroy()
                for s in self.getSpritesbyClass(sprong):
                    s.destroy()
                for s in self.getSpritesbyClass(textbox):
                    s.destroy()
                for s in self.getSpritesbyClass(Snake):
                    s.destroy()
                for s in self.getSpritesbyClass(Snakebox):
                    s.destroy()
                for s in self.getSpritesbyClass(Platform):
                    s.destroy()
                if self.levelindex>.5:
                    self.levelindex-=.5
  
        for ship in self.getSpritesbyClass(Player):
            ship.step()
        for p in self.getSpritesbyClass(Snake):
            p.step()
        for p in self.getSpritesbyClass(Snakebox):
            p.step()
        for p in self.getSpritesbyClass(Platform):
            p.step()
print("use the left and right arrows to move , space bar to jump, and down arrow when sliding on a wall to wall")        
myapp = SpaceGame()
myapp.run()