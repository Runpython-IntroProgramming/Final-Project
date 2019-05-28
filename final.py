#kyDoleuc04
#Final Project

from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, Frame, TextAsset

pink = Color(0xFF00FF, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x39ff14, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
grey = Color(0xC0C0C0, 1.0)
yellow = Color(0xffff00, 1.0)

class Bird(Sprite):
    side = LineStyle(1,black)
    poly = RectangleAsset(10,10, side, yellow)
    def __init__(self,position):
        super().__init__(Bird.poly,position)
        self.vx = 0
        self.vy = 0

class Block(Sprite):
    side = LineStyle(1,black)
    square = RectangleAsset(30,30,side,green)
    def __init__(self,position):
        super().__init__(Block.square,position)

class Game(App):
    def __init__(self):
        super().__init__(1000,540)
    
        Game.listenKeyEvent('keydown', 'right arrow',  self.right)
        Game.listenKeyEvent('keyup', 'right arrow',  self.rightstop)
        Game.listenKeyEvent('keydown', 'left arrow',  self.left)
        Game.listenKeyEvent('keyup', 'left arrow',  self.leftstop)
        Game.listenKeyEvent('keydown', 'up arrow',  self.up)
        Game.listenKeyEvent('keyup', 'up arrow',  self.upstop)
        Game.listenKeyEvent('keydown', 'down arrow',  self.down)
        Game.listenKeyEvent('keyup', 'down arrow',  self.downstop)   
        
        x = 0
        y = 0
        
        Bird((10,250))
        Block((75,100))
        Block((75,130))
        Block((75,160))
        
    def right(self,event):
        for sprite in self.getSpritesbyClass(Bird):
            sprite.vx = 2
            
    def rightstop(self,event):
        for sprite in self.getSpritesbyClass(Bird):
            sprite.vx = 0
            
    def left(self,event):
        for sprite in self.getSpritesbyClass(Bird):
            sprite.vx = -2
            
    def leftstop(self,event):
        for sprite in self.getSpritesbyClass(Bird):
            sprite.vx = 0
    
    def up(self,event):
        #if self.grounded == True: 
            for sprite in self.getSpritesbyClass(Bird):
                sprite.vy = -5
    
    def upstop(self,event):
        for sprite in self.getSpritesbyClass(Bird):
            sprite.vy = 0
            
    def down(self,event):
        for sprite in self.getSpritesbyClass(Bird):
            sprite.vy = 2
    
    def downstop(self,event):
        for sprite in self.getSpritesbyClass(Bird):
            sprite.vy = 0
            
   

myapp = Game()
myapp.run()