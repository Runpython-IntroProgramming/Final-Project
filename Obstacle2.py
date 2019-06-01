from ggame import App, Sprite, ImageAsset, Frame, CircleAsset
from ggame import SoundAsset, Color, LineStyle, TextAsset, Sound
import math
from time import time
from ggame.sysdeps import SND_Sound
SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 700

myapp = App()


print("Press enter to play")


class SpaceShip(Sprite):
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')
    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0.005
        self.thrust = 0
        self.thrustframe = 0
        Obstacle.listenKeyEvent("keydown", "w", self.thrustOn)
        Obstacle.listenKeyEvent("keyup", "w", self.thrustOff)
        Obstacle.listenKeyEvent("keydown", "a", self.right)
        Obstacle.listenKeyEvent("keyup", "a", self.stop)
        Obstacle.listenKeyEvent("keydown", "d", self.left)
        Obstacle.listenKeyEvent("keyup", "d", self.stop)
        self.fxcenter = self.fycenter = 0.5
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 0.8
            self.vx += 0.03*math.cos(self.rotation+1/2*math.pi)
            self.vy += 0.03*math.sin(self.rotation-1/2*math.pi)
            if self.thrustframe == 4:
                self.thrustframe = 1
            else:
                self.setImage(3.9)
                nba=self.collidingWithSprites(finish)
                omg=self.collidingWithSprites(finish2)
                tehe=self.collidingWithSprites(finish3)
                hg=self.collidingWithSprites(finish4)
                if nba:
                    print('You Win, Press 1 for Next Level')
                if omg:
                    print('You Win, Press r for Next Level')
                if tehe:
                    print('You Win, Press g for Next Level')
                if hg:
                    print('You Win, Press k for Next Level')
            
            self.setImage(3.9)
        lol=self.collidingWithSprites(obstacle1)
        gg=self.collidingWithSprites(orangefish)
        hg=self.collidingWithSprites(bluefish)
        cn=self.collidingWithSprites(coconut)
        oo=self.collidingWithSprites(cloud)
        ee=self.collidingWithSprites(cloud2)
        aa=self.collidingWithSprites(cloud3)
        ata=self.collidingWithSprites(cloud4)
        atta=self.collidingWithSprites(cloud5)
        if lol:
            self.explode(self)
            print('GG You Lost')
        if gg:
            self.explode(self)
            print('GG You Lost')
        if hg:
            self.explode(self)
            print('GG You Lost')
        if cn:
            self.explode(self)
            print('GG You Lost')
        if oo:
            self.explode(self)
            print('GG You Lost')
        if ee:
            self.explode(self)
            print('GG You Lost')
        if aa:
            self.explode(self)
            print('GG You Lost')
        if ata:
            self.explode(self)
            print('GG You Lost')
        if atta:
            self.explode(self)
            print('GG You Lost')
            

    def thrustOn(self, event):
        self.thrust = 1

    def thrustOff(self, event):
        self.thrust = 0

    def up(self, event):
        self.vy=1 
    def down(self, event):
        self.vy=-1
    def right(self, event):
        self.vr = .1
    def left(self, event):
        self.vr = -.1
    def stop(self, event):
        self.vr=0

    def explode(self, event):
        self.visible = False
        self.vx=0
        self.vy=0
        explosionn(self.position)
    def Win(self, event):
        self.visible = false
        self.vx=0
        self.vy=0
        explosionn(self.position)
        
        
class explosionn(Sprite):
    
    asset = ImageAsset("images/explosion1.png", Frame(0,0,128,128), 10)
   
    def __init__(self, position):
        super().__init__(explosionn.asset, position)
        self.image = 0
        self.center = (0.5, 0.5)
    def step(self):
        self.setImage(self.image//2)
        self.image = self.image + 1
        if self.image == 10:
            self.destroy()
    
class Obstacle(App):
   
    def __init__(self, width, height):
        super().__init__(width, height)
        mario((5,40))
        mariodirections((40,180))
        mariow((40,250))
        mariofor((457,250))
        marioa((40,320))
        mariod((40,390))
        marioop((0,0))
        Obstacle.listenKeyEvent("keydown", "enter", self.level1)
        Obstacle.listenKeyEvent("keydown", "1", self.level2)
        Obstacle.listenKeyEvent("keydown", "r", self.level3)
        Obstacle.listenKeyEvent("keydown", "g", self.level4)
        Obstacle.listenKeyEvent("keydown", "k", self.level5)
        
    
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
        for explosion in self.getSpritesbyClass(explosionn):
            explosion.step()
    
    def level1(self,event):
        for s in self.getSpritesbyClass(mario):
            s.destroy()
        for s in self.getSpritesbyClass(mariow):
            s.destroy()   
        for s in self.getSpritesbyClass(mariofor):
            s.destroy()
        for s in self.getSpritesbyClass(mariodirections):
            s.destroy()
        for s in self.getSpritesbyClass(mariod):
            s.destroy()
        for s in self.getSpritesbyClass(marioa):
            s.destroy()
        for s in self.getSpritesbyClass(marioop):
            s.destroy()
            Beach((0,0))
            finish((650,300))
            obstacle1((800,50))
            obstacle1((80,400))
            Tsunami((200,2))
            finishh((750,397))
            SpaceShip((20,10))
    
    def level2(self,event):
        for x in self.getSpritesbyClass(finish):
            x.destroy()
        for x in self.getSpritesbyClass(obstacle1):
            x.destroy()
        for x in self.getSpritesbyClass(Beach):
            x.destroy()
        for x in self.getSpritesbyClass(Tsunami):
            x.destroy()
        for x in self.getSpritesbyClass(SpaceShip):
            x.destroy()
        for x in self.getSpritesbyClass(finishh):
            x.destroy()
            background2((0,0))
            Coral((200,2))
            orangefish((50,400))
            bluefish((300,150))
            finish2((900,200))
            finishh2((960,260))
            SpaceShip((10,10))
    def level3(self,event):
        for q in self.getSpritesbyClass(background2):
            q.destroy()
        for q in self.getSpritesbyClass(SpaceShip):
            q.destroy()
        for q in self.getSpritesbyClass(orangefish):
            q.destroy()
        for q in self.getSpritesbyClass(bluefish):
            q.destroy()
        for q in self.getSpritesbyClass(finish2):
            q.destroy()
        for q in self.getSpritesbyClass(Coral):
            q.destroy()
        for q in self.getSpritesbyClass(finishh2):
            q.destroy()   
            background3((0,0))
            coconut((100,100))
            coconut((300,200))
            coconut((200,400))
            coconut((700,100))
            coconut((700,500))
            Valley((200,2))
            SpaceShip((10,10))
            finish3((900,200))
            finishh3((960,260))
    def level4(self,event):
        for t in self.getSpritesbyClass(background3):
            t.destroy()
        for t in self.getSpritesbyClass(SpaceShip):
            t.destroy()
        for t in self.getSpritesbyClass(finish3):
            t.destroy()
        for t in self.getSpritesbyClass(coconut):
            t.destroy()
        for t in self.getSpritesbyClass(Valley):
            t.destroy()
        for t in self.getSpritesbyClass(finishh3):
            t.destroy()
        
            
            background4((0,0))
            finish4((30,400))
            finishh4((92.5,460))
            SpaceShip((400,10))
            cloud((7,58))
            cloud2((177,197))
            cloud3((512,100))
            cloud4((956,35))
            cloud5((743,210))
            hilly((580,550))
    def level5(self,event):
        for i in self.getSpritesbyClass(background4):
            i.destroy()
        for i in self.getSpritesbyClass(finish4):
            i.destroy()
        for i in self.getSpritesbyClass(SpaceShip):
            i.destroy()
        for i in self.getSpritesbyClass(cloud):
            i.destroy()
        for i in self.getSpritesbyClass(cloud2):
            i.destroy()
        for i in self.getSpritesbyClass(cloud3):
            i.destroy()
        for i in self.getSpritesbyClass(cloud4):
            i.destroy()
        for i in self.getSpritesbyClass(cloud5):
            i.destroy()
        for i in self.getSpritesbyClass(finishh4):
            i.destroy()
        for i in self.getSpritesbyClass(hilly):
            i.destroy()
        SpaceShip((10,10))


#LEVEL ONE:     
class obstacle1(Sprite):
    hi = ImageAsset("images/beach-ball-575425_640.png")
    def __init__(self, position):
        super().__init__(obstacle1.hi, position)
        self.scale = 0.2
class finish(Sprite):
    op = ImageAsset("images/FinishLine1.png")
    def __init__(self, position):
        super().__init__(finish.op, position)
        self.scale = 0.8
class Beach(Sprite):
    cool = ImageAsset("images/cartoon-beach-clipart-6.jpg")
    def __init__(self, position):
        super().__init__(Beach.cool, position)
        self.scale = 0.6
class Tsunami(Sprite):
    o = ImageAsset("images/Screenshot 2019-05-29 at 9.57.01 AM.png")
    def __init__(self, position):
        super().__init__(Tsunami.o, position)
        self.scale = 0.8
class mario(Sprite):
    wo = ImageAsset("images/Screenshot 2019-05-29 at 4.45.47 PM.png")
    def __init__(self, position):
        super().__init__(mario.wo, position)
        self.scale = 1.4
class mariodirections(Sprite):
    woo = ImageAsset("images/Screenshot 2019-05-29 at 5.06.55 PM.png")
    def __init__(self, position):
        super().__init__(mariodirections.woo, position)
        self.scale = 0.7
class mariow(Sprite):
    wow = ImageAsset("images/Screenshot 2019-05-29 at 5.07.34 PM.png")
    def __init__(self, position):
        super().__init__(mariow.wow, position)
        self.scale = 0.6
class mariofor(Sprite):
    fo = ImageAsset("images/Screenshot 2019-05-29 at 5.07.51 PM.png")
    def __init__(self, position):
        super().__init__(mariofor.fo, position)
        self.scale = 0.6
class marioa(Sprite):
    aaa = ImageAsset("images/Screenshot 2019-05-29 at 5.19.49 PM.png")
    def __init__(self, position):
        super().__init__(marioa.aaa, position)
        self.scale = 0.6
class mariod(Sprite):
    dd = ImageAsset("images/Screenshot 2019-05-29 at 5.29.45 PM.png")
    def __init__(self, position):
        super().__init__(mariod.dd, position)
        self.scale = 0.6
class finishh(Sprite):
    rr = ImageAsset("images/Screenshot 2019-05-29 at 6.06.04 PM.png")
    def __init__(self, position):
        super().__init__(finishh.rr, position)
        self.scale = 0.8
class finishh2(Sprite):
    rer = ImageAsset("images/Screenshot 2019-05-29 at 6.06.04 PM.png")
    def __init__(self, position):
        super().__init__(finishh2.rer, position)
        self.scale = 0.5
class finishh3(Sprite):
    reyr = ImageAsset("images/Screenshot 2019-05-29 at 6.06.04 PM.png")
    def __init__(self, position):
        super().__init__(finishh3.reyr, position)
        self.scale = 0.5
class finishh4(Sprite):
    ryr = ImageAsset("images/Screenshot 2019-05-29 at 6.06.04 PM.png")
    def __init__(self, position):
        super().__init__(finishh4.ryr, position)
        self.scale = 0.5
class marioop(Sprite):
    ryer = ImageAsset("images/MARIO.png")
    def __init__(self, position):
        super().__init__(marioop.ryer, position)
        self.scale = 0.1
        
#LEVEL TWO:
class background2(Sprite):
    nba= ImageAsset("images/UnderWater.jpg")
    def __init__(self, position):
        super().__init__(background2.nba, position)
        self.scale = 1.3
class orangefish(Sprite):
    cool= ImageAsset("images/OPOrangeFish.png")
    def __init__(self, position):
        super().__init__(orangefish.cool, position)
        self.scale = 0.2
class bluefish(Sprite):
    math= ImageAsset("images/OPBlueFish.png")
    def __init__(self, position):
        super().__init__(bluefish.math, position)
        self.scale = 0.6
class finish2(Sprite):
    hehe = ImageAsset("images/Finish2.png")
    def __init__(self, position):
        super().__init__(finish2.hehe, position)
        self.scale = 0.5
class Coral(Sprite):
    e = ImageAsset("images/Screenshot 2019-05-29 at 10.03.18 AM.png")
    def __init__(self, position):
        super().__init__(Coral.e, position)
        self.scale = 0.8






#LEVEL THREE:
class background3(Sprite):
    hahaha= ImageAsset("images/Background3.jpg")
    def __init__(self, position):
        super().__init__(background3.hahaha, position)
        self.scale = 2.5
class finish3(Sprite):
    col= ImageAsset("images/FinishLine3.png")
    def __init__(self, position):
        super().__init__(finish3.col, position)
        self.scale = 0.5
class coconut(Sprite):
    ligma= ImageAsset("images/GC.png")
    def __init__(self, position):
        super().__init__(coconut.ligma, position)
        self.scale = 0.1
class Valley(Sprite):
    t = ImageAsset("images/Screenshot 2019-05-29 at 10.08.08 AM.png")
    def __init__(self, position):
        super().__init__(Valley.t, position)
        self.scale = 0.8     
"""class yip:
    Yip = SoundAsset("sounds/mk64_mario10.wav")
 """   

#LEVEL FOUR:
class background4(Sprite):
    hahah= ImageAsset("images/background4.jpg")
    def __init__(self, position):
        super().__init__(background4.hahah, position)
        self.scale = 1
class cloud(Sprite):
    hahh= ImageAsset("images/Cloud.png")
    def __init__(self, position):
        super().__init__(cloud.hahh, position)
        self.scale = 0.73
class cloud2(Sprite):
    hah= ImageAsset("images/Cloud.png")
    def __init__(self, position):
        super().__init__(cloud2.hah, position)
        self.scale = 0.85
class cloud3(Sprite):
    heh= ImageAsset("images/Cloud.png")
    def __init__(self, position):
        super().__init__(cloud3.heh, position)
        self.scale = 0.84
class cloud4(Sprite):
    hih= ImageAsset("images/Cloud.png")
    def __init__(self, position):
        super().__init__(cloud4.hih, position)
        self.scale = 0.65
class cloud5(Sprite):
    hoh= ImageAsset("images/Cloud.png")
    def __init__(self, position):
        super().__init__(cloud5.hoh, position)
        self.scale = 1.1
class finish4(Sprite):
    cole= ImageAsset("images/FinishLine3.png")
    def __init__(self, position):
        super().__init__(finish4.cole, position)
        self.scale = 0.5
class hilly(Sprite):
    td = ImageAsset("images/Screenshot 2019-05-29 at 9.20.02 PM.png")
    def __init__(self, position):
        super().__init__(hilly.td, position)
        self.scale = 0.8  
myapp = Obstacle(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
