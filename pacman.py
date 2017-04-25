from ggame import App, RectangleAsset, ImageAsset, SoundAsset, CircleAsset
from ggame import LineStyle, Color, Sprite, Sound

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
up=0

blue=Color(0x87cefa, 1)
purple=Color(0x7b68ee, 1)
line=LineStyle(0,blue)
white = Color(0xfffafa,1)
green = Color(0x00ff00, 1)
black = Color(0, 1)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, line, black)
bg = Sprite(bg_asset, (0,0))

vline=RectangleAsset(2,50,line,white)
hline=RectangleAsset(50,2,line,white)
 
Sprite(vline,(50,50))
Sprite(vline,(50,100))
Sprite(vline,(50,150))
Sprite(vline,(50,250))
Sprite(vline,(50,300))
Sprite(hline, (100,50))
Sprite(hline, (50,200))
Sprite(hline, (50,250))
Sprite(hline, (300,200))

pman=Sprite(CircleAsset(15,line,purple),(25,25))
pman.dir=0
pman.go = True    

def leftKey(event):
    global up
    pman.dir=-4
    up=0
def rightKey(event):
    global up
    pman.dir=4
    up=0    
def upKey(event):
    global up
    pman.dir=-4
    up=1
def downKey(event):
    global up
    pman.dir=4
    up=1
def step():
    global up
    if pman.go:
        if up==0:
            pman.x += pman.dir
        if up==1:
            pman.y += pman.dir
        
myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run(step)
myapp.listenKeyEvent('keydown', 'j', leftKey)
myapp.listenKeyEvent('keydown', 'i', upKey)
myapp.listenKeyEvent('keydown', 'k', downKey)
myapp.listenKeyEvent('keydown', 'l', rightKey)
