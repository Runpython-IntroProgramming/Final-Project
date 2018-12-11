#Ella Edmonds Final Project
#Fireboy and Water Girl

from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

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
    grey = Color(0xC0C0C0, 1.0)
    black = Color(0x000000, 1.0)
    side = LineStyle(1,grey)
    square = RectangleAsset(30,30,side,black)
    def __init__(self,position):
        super().__init__(Block.square,position)

#Block((60,60))
#Grid((60,60))
#Sprite(grid,(30,30))


class Game(App):
    
    def __init__(self):
        super().__init__()
        Game.listenMouseEvent("click",self.block)
    
    Cells = []
    def __init__(self):
        
        super().__init__()
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
            
        #print(self.Cells)
    
    def block(self,event):
        print("hi")
        for m in self.Cells:
            if m[0] <= event.x <= m[0]+30:
                if m[1] <= event.y <= m[1]+30:
                    Block((m[0],m[1]))
    



myapp = Game()
myapp.run()