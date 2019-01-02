#Ella Edmonds Final Project
#Fireboy and Water Girl
#Sources: Noah and Katie

from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, Frame, TextAsset

print("Use right, left and up arrows to move the player.")
print("     -if stuck press the up arrow")
print()
print("Try and collect as many gems as possible.")
print()
print("If you land on the pink spikes you die.")
print()
print("You can end the game by running into either of the two purple blocks in the top corners.")
print()
print("You win the game if you can collect all 10 gems!")
print()
print("p.s. if you're frustrated and want to cheat just comment out line 330 :)")

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

blue = Color(0x2EFEC8, 1.0)
black = Color(0x000000, 1.0)
pink = Color(0xFF00FF, 1.0)
red = Color(0xFF5733, 1.0)
white = Color(0xFFFFFF, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
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
grid = RectangleAsset(30,30,gridline,red)


class Grid(Sprite):
    grey = Color(0xC0C0C0, 1.0)
    white = Color(0xffffff, 1.0)
    side = LineStyle(1,grey)
    square = RectangleAsset(30,30,side,white)
    def __init__(self,position):
        super().__init__(Grid.square,position)

class Block(Sprite):
    black = Color(0x000000, 1.0)
    side = LineStyle(1,black)
    square = RectangleAsset(30,30,side,black)
    def __init__(self,position):
        super().__init__(Block.square,position)

class BottomSpike(Sprite):
    pink = Color(0xFF00FF, .5)
    side = LineStyle(1,pink)
    poly = PolygonAsset([(0, 0),(30,0),(15,-20)], side, pink)
    def __init__(self,position):
        super().__init__(BottomSpike.poly,position)
        
class Spikes(Sprite):
    pink = Color(0xFF00FF, .5)
    side = LineStyle(1,pink)
    poly = PolygonAsset([(0, 0),(5,-10),(10,0),(15,-10),(20,0),(25,-10),(30,0)], side, pink)
    def __init__(self,position):
        super().__init__(Spikes.poly,position)
        
class Gem(Sprite):
    green = Color(0x00ff00, .5)
    side = LineStyle(1,green)
    poly = PolygonAsset([(0, 0),(5,-10),(10,0),(5,10)], side, green)
    def __init__(self,position):
        super().__init__(Gem.poly,position)
   
class Person(Sprite):
    blue = Color(0x0000CF, .5)
    side = LineStyle(1,blue)
    poly = RectangleAsset(10,10, side, blue)
    def __init__(self,position):
        super().__init__(Person.poly,position)
        self.vx = 0
        self.vy = 0
        
class Sideleft(Sprite):
    blue = Color(0x0000CF, .5)
    side = LineStyle(1,blue)
    poly = RectangleAsset(1,8, side, blue)
    def __init__(self,position):
        super().__init__(Sideleft.poly,position)
        self.vx = 0
        self.vy = 0

class Sideright(Sprite):
    blue = Color(0x0000CF, .5)
    side = LineStyle(1,blue)
    poly = RectangleAsset(1,8, side, blue)
    def __init__(self,position):
        super().__init__(Sideright.poly,position)
        self.vx = 0
        self.vy = 0

class Top(Sprite):
    blue = Color(0x0000CF, .5)
    side = LineStyle(1,blue)
    poly = RectangleAsset(8,1, side, blue)
    def __init__(self,position):
        super().__init__(Top.poly,position)
        self.vx = 0
        self.vy = 0
        
class bottom(Sprite):
    blue = Color(0x0000CF, .5)
    side = LineStyle(1,blue)
    poly = RectangleAsset(8,1, side, blue)
    def __init__(self,position):
        super().__init__(bottom.poly,position)
        self.vx = 0
        self.vy = 0

class finish(Sprite):
    purple = Color(0x380966, .7)
    side = LineStyle(1,purple)
    poly = RectangleAsset(10,40, side, purple)
    def __init__(self,position):
        super().__init__(finish.poly,position)
        self.vx = 0
        self.vy = 0

class Game(App):
    Cells = []
    def __init__(self):
        super().__init__()
        
        self.gameover = False
        gemgotlist  = []
        self.grounded = False
        self.dead = False
        
        #Game.listenMouseEvent("click",self.block)
        Game.listenKeyEvent('keydown', 'right arrow',  self.right)
        Game.listenKeyEvent('keyup', 'right arrow',  self.rightstop)
        Game.listenKeyEvent('keydown', 'left arrow',  self.left)
        Game.listenKeyEvent('keyup', 'left arrow',  self.leftstop)
        Game.listenKeyEvent('keydown', 'up arrow',  self.up)
        Game.listenKeyEvent('keyup', 'up arrow',  self.upstop)
        Game.listenKeyEvent('keydown', 'down arrow',  self.down)
        Game.listenKeyEvent('keyup', 'down arrow',  self.downstop)
    
        x=0
        y=0
        for b in range(18):
            for a in range(25):
                Grid((x,y))
                #print((x,y))
                self.Cells.append((x,y))
                x = x + 30
            x = 0
            Grid((x,y))
            #print((x,y))
            self.Cells.append((x,y))
            y = y + 30
        Block((0, 480))
        Block((30, 480))
        Block((60, 480))
        Block((120, 450))
        Block((180, 450))
        Block((240, 450))
        Block((300, 480))
        Block((330, 480))
        Block((360, 480))
        Block((360, 450))
        Block((390, 390))
        Block((390, 420))
        Block((390, 450))
        Block((390, 480))
        Block((420, 390))
        Block((450, 390))
        Block((480, 390))
        Block((390, 330))
        Block((360, 330))
        Block((330, 330))
        Block((300, 330))
        Block((270, 300))
        Block((240, 300))
        Block((210, 300))
        Block((150, 300))
        Block((90, 300))
        Block((120, 300))
        Block((60, 270))
        Block((30, 240))
        Block((0, 210))
        Block((120, 210))
        Block((90, 210))
        Block((150, 180))
        Block((180, 180))
        Block((210, 150))
        Block((240, 150))
        Block((30, 90))
        Block((0, 90))
        Block((60, 90))
        Block((90, 90))
        Block((120, 90))
        Block((150, 90))
        Block((0, 60))
        Block((540, 480))
        Block((570, 450))
        Block((600, 420))
        Block((630, 390))
        Block((660, 390))
        Block((690, 390))
        Block((720, 390))
        Block((660, 330))
        Block((630, 330))
        Block((600, 330))
        Block((570, 330))
        Block((540, 300))
        Block((510, 270))
        Block((480, 240))
        Block((450, 240))
        Block((420, 240))
        Block((390, 240))
        Block((390, 210))
        Block((450, 150))
        Block((480, 150))
        Block((510, 150))
        Block((720, 90))
        Block((690, 90))
        Block((660, 90))
        Block((630, 90))
        Block((600, 90))
        Block((570, 90))
        Block((720, 60))
        Block((210, 60))
        Block((270, 60))
        Block((330, 60))
        Block((390, 60))
        Block((450, 60))
        Block((510, 60))
        Block((270, 120))
        Block((330, 150))
        Block((360, 150))
        Block((390, 120))
        Block((630, 240))
        Block((660, 240))
        Block((690, 240))
        Block((720, 240))
        Block((600, 240))
        Block((570, 240))
        Block((630, 180))
        Block((660, 180))
        Block((690, 180))
        Block((720, 180))
        Block((570, 150))
        Block((480, 480))
        Block((510, 480))
        Block((300,120))
        
        for m in range(25):
            BottomSpike((m*30,520))
            
        for m in range(25):
            BottomSpike((m*30,-25))
            
        for m in range(40):
            BottomSpike((m*30,680))
            
        for m in range(10):
            BottomSpike((m*-30,680))
            
        for m in range(27):
            BottomSpike((-30,m*20))
            
        Spikes((90, 80))
        Spikes((630, 80))
        Spikes((120, 290))
        Spikes((600, 320))
        Spikes((720, 380))
        Spikes((450, 380))
        Spikes((300, 320))
        Spikes((360, 320))
        Spikes((240, 290))
        
        Gem((40, 460))
        Gem((40, 215))
        Gem((280, 95))
        Gem((340, 35))
        Gem((460, 35))
        Gem((700, 155))
        Gem((490, 455))
        Gem((190, 425))
        Gem((10, 155))
        Gem((730, 335))
        
        finish((10,10))
        finish((730,10))
        
        Person((10,450))
        Sideleft((10,451))
        Sideright((20,451))
        Top((11,450))
        bottom((11,460))

        #print(self.Cells)
    
    
    def right(self,event):
        for sprite in self.getSpritesbyClass(Person):
            sprite.vx = 2
            
    def rightstop(self,event):
        for sprite in self.getSpritesbyClass(Person):
            sprite.vx = 0
            
    def left(self,event):
        for sprite in self.getSpritesbyClass(Person):
            sprite.vx = -2
            
    def leftstop(self,event):
        for sprite in self.getSpritesbyClass(Person):
            sprite.vx = 0
    
    def up(self,event):
        if self.grounded == True: 
            for sprite in self.getSpritesbyClass(Person):
                sprite.vy = -5
    
    def upstop(self,event):
        for sprite in self.getSpritesbyClass(Person):
            sprite.vy = 0
            
    def down(self,event):
        for sprite in self.getSpritesbyClass(Person):
            sprite.vy = 2
    
    def downstop(self,event):
        for sprite in self.getSpritesbyClass(Person):
            sprite.vy = 0
    
    text=Sprite(TextAsset("GEMS:{0}".format(0), width=1000, align='center',style='30px Arial', fill=Color(0x2C2D5E,1)), (760,10))
    gemgot = 0
    def step(self):
        
        for sprite in self.getSpritesbyClass(Person):
            #Sprite.vy+=1
            for gem in self.getSpritesbyClass(Gem)[:]:
                if gem.collidingWithSprites(Person):
                    #print("You get a gem")
                    self.text.destroy()
                    self.gemgot += 1
                    self.text=Sprite(TextAsset("GEMS:{0}".format(self.gemgot), width=1000, align='center',style='30px Arial', fill=Color(0x2C2D5E,1)), (760,10))
                    gem.destroy()
                    if self.gemgot == 10:
                        self.gameover=True
            
            for a in self.getSpritesbyClass(Sideright):
                if a.collidingWithSprites(Block):
                    sprite.x -= 1
                    sprite.vx = 0
                    a.vx = 0
                    
            for b in self.getSpritesbyClass(Sideleft):
                if b.collidingWithSprites(Block):
                    sprite.x += 1
                    sprite.vx = 0
                    b.vx = 0
                   
            for c in self.getSpritesbyClass(Top):
                #print(c.collidingWithSprites(Block))
                if c.collidingWithSprites(Block):
                    #print(c.collidingWithSprites(Block))
                    sprite.y += 1
                    sprite.vy = 0
                    c.vy = 0
            
            for d in self.getSpritesbyClass(bottom):
                #print(d.collidingWithSprites(Block))
                if d.collidingWithSprites(Block) == []:
                    sprite.vy += .2
                    self.grounded = False
                else:
                    if sprite.vy < 0:
                        sprite.vy = sprite.vy
                        self.grounded = True
                    #elif sprite.vy > 0:
                        #sprite.vy = sprite.vy
                        #self.grounded = True
                    else:
                        sprite.vy = 0
                        self.grounded = True
                
            for e in self.getSpritesbyClass(bottom):
                if e.collidingWithSprites(BottomSpike):
                    sprite.y += 0
                    sprite.vy = 0
                    sprite.x += 0
                    sprite.vx = 0
                    self.gameover = True
                    self.dead = True
                    
            for f in self.getSpritesbyClass(bottom):
                if e.collidingWithSprites(Spikes):
                    sprite.y += 0
                    sprite.vy = 0
                    sprite.x += 0
                    sprite.vx = 0
                    self.gameover = True
                    self.dead = True
                    
            for f in self.getSpritesbyClass(bottom):
                if e.collidingWithSprites(finish):
                    sprite.y += 0
                    sprite.vy = 0
                    sprite.x += 0
                    sprite.vx = 0
                    self.gameover = True
                    
            #if sprite.vy < -3:
                #sprite.vy=-3
                    
            #for d in self.getSpritesbyClass(bottom):
             #   if d.collidingWithSprites(Bottom):
              #      d.vy >= 0
               #     Sprite.vy >= 0
                    
            sprite.x += sprite.vx 
            sprite.y += sprite.vy
            
            for a in self.getSpritesbyClass(Sideleft):
                a.x = sprite.x
                a.y = sprite.y+1
            for b in self.getSpritesbyClass(Sideright):
                b.x = sprite.x+10
                b.y = sprite.y+1
            for c in self.getSpritesbyClass(Top):
                c.x = sprite.x+1
                c.y = sprite.y
            for d in self.getSpritesbyClass(bottom):
                d.x = sprite.x+1
                d.y = sprite.y+10
                
        if self.gameover:
            if self.dead == True:
                self.text=Sprite(TextAsset("GAME OVER :(", width=1000, align='center',style='30px Arial', fill=Color(0xff2222,1)), (760,50))
                myapp.gameover=True
            elif self.gemgot <= 5:
                self.text=Sprite(TextAsset("You Ended the Game", width=1000, align='center',style='30px Arial', fill=Color(0x9A9CE5,1)), (760,50))
                self.text=Sprite(TextAsset("Grade: F :(", width=1000, align='center',style='30px Arial', fill=Color(0xA7A8BC,1)), (760,90))
                myapp.gameover=True
            elif self.gemgot == 6:
                self.text=Sprite(TextAsset("You Ended the Game", width=1000, align='center',style='30px Arial', fill=Color(0x9A9CE5,1)), (760,50))
                self.text=Sprite(TextAsset("Grade: D :(", width=1000, align='center',style='30px Arial', fill=Color(0xA7A8BC,1)), (760,90))
                myapp.gameover=True
            elif self.gemgot == 7:
                self.text=Sprite(TextAsset("You Ended the Game", width=1000, align='center',style='30px Arial', fill=Color(0x9A9CE5,1)), (760,50))
                self.text=Sprite(TextAsset("Grade: C :/", width=1000, align='center',style='30px Arial', fill=Color(0xA7A8BC,1)), (760,90))
                myapp.gameover=True
            elif self.gemgot == 8:
                self.text=Sprite(TextAsset("You Ended the Game", width=1000, align='center',style='30px Arial', fill=Color(0x9A9CE5,1)), (760,50))
                self.text=Sprite(TextAsset("Grade: B :/", width=1000, align='center',style='30px Arial', fill=Color(0xA7A8BC,1)), (760,90))
                myapp.gameover=True
            elif self.gemgot == 9:
                self.text=Sprite(TextAsset("You Ended the Game", width=1000, align='center',style='30px Arial', fill=Color(0x9A9CE5,1)), (760,50))
                self.text=Sprite(TextAsset("Grade: A- :)", width=1000, align='center',style='30px Arial', fill=Color(0xA7A8BC,1)), (760,90))
                myapp.gameover=True
            elif self.gemgot == 10:
                self.text=Sprite(TextAsset("You Win :)", width=1000, align='center',style='30px Arial', fill=Color(0x00ff00, 1.0)), (760,50))
                myapp.gameover=True
            

            
    
    
    #def jump(self,event):
        
    
    '''def block(self,event):
        #print("hi")
        for m in self.Cells:
            if m[0] <= event.x <= m[0]+30:
                if m[1] <= event.y <= m[1]+30:
                    Block((m[0],m[1]))
                    print((m[0],m[1]))'''
    



myapp = Game()
myapp.run()