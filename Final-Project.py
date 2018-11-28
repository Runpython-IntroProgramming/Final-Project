from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame

blue = Color(0x2EFEC8, 1.0)
black = Color(0x000000, 1.0)
pink = Color(0xFF00FF, 1.0)
red = Color(0xFF5733, 1.0)
white = Color(0xFFFFFF, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x009933, 1.0)
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
        sunflower_asset.scale = 0.15
        super().__init__(sunflower_asset, position)

# PvZ---------------------------------------------------------------------------

class PvZ(App):
    def __init__(self):
            super().__init__()
        
# House-------------------------------------------------------------------------
            background = ImageAsset("images/1.jpg")
            backgroundscale=Sprite(background)
            backgroundscale.scale = 1.5
            
            houseroof1 = RectangleAsset(100, 125, thinline, lightbrown)
            Sprite(houseroof1,(20,85))
            houseroof2 = RectangleAsset(100, 125, thinline, lightbrown2)
            Sprite(houseroof2,(20,210))
            
            houseroof3 = RectangleAsset(100, 125, thinline, lightbrown)
            Sprite(houseroof3,(20,410))
            houseroof4 = RectangleAsset(100, 125, thinline, lightbrown2)
            Sprite(houseroof4,(20,535))
            
            houseroof5 = RectangleAsset(200, 325, thinline, lightbrown)
            Sprite(houseroof5,(-150,45))
            houseroof6 = RectangleAsset(200, 325, thinline, lightbrown2)
            Sprite(houseroof6,(-150,370))
            
# Grid--------------------------------------------------------------------------
            
            grid = RectangleAsset(110,110,whiteline,tile1)
            grid2 = RectangleAsset(110,110,whiteline,tile2)
            x = 150 
            y = 95
            for a in range(10):
                Sprite(grid2,(x,y))
                x = x + 110
            
            c = 150 
            d = 110+95
            for a in range(10):
                Sprite(grid,(c,d))
                c = c + 110
             
            e = 150 
            f = 2*(110)+95
            for a in range(10):
                Sprite(grid2,(e,f))
                e = e + 110
             
            g = 150 
            h = 3*(110)+95
            for a in range(10):
                Sprite(grid,(g,h))
                g = g + 110
             
            k = 150 
            l = 4*(110)+95
            for a in range(10):
                Sprite(grid2,(k,l))
                k = k + 110
# Function Calling--------------------------------------------------------------
            PvZ.listenMouseEvent("mousemove", self.moveMouse)
            PvZ.listenKeyEvent('keydown', 's', self.sunflowerplacement) 
            
# Functions---------------------------------------------------------------------
            x=0
            y=0
            
        def moveMouse(self, event):
                self.x = event.x
                self.y = event.y
            
        def sunflowerplacement(self,event):
            Sunflower((0,0))


            
myapp = PvZ()
myapp.run()
