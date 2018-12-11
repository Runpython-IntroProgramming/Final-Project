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
grid = RectangleAsset(30,30,gridline,white)

class Grid(Sprite):
    white = Color(0xffffff, 1.0)
    grey = Color(0xC0C0C0, 1.0)
    gridline = LineStyle(1, grey)
    grid = RectangleAsset(30,30,gridline,red)
    
    def __init__(self,position):
        super.__init__(Grid.grid,position)
        self.vx = (position)

Grid((0,0))

class FireBoy(Sprite):
    Fireboy = RectangleAsset(15,35, noline,pink)
    
    def __init__(self, position):
        super.__init__(FireBoy.Fireboy,position)
        FireBoy = Sprite(Fireboy,position)
        

class Game(App):
    def __init__(self):
        
        super().__init__()
        x=0
        y=0
        for b in range(18):
            for a in range(25):
                Sprite(grid, (x,y))
                x = x + 30
            x = 0
            Sprite(grid,(x,y))
            y = y + 30
    




myapp = Game()
myapp.run()