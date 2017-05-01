
from ggame import App, RectangleAsset, ImageAsset, SoundAsset, CircleAsset
from ggame import LineStyle, Color, Sprite, Sound
from random import randint

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
up=5
speed=3
blue=Color(0x87cefa, 1)
purple=Color(0x7b68ee, 1)
line=LineStyle(0,blue)
black = Color(0, 1)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, line, black)
bg = Sprite(bg_asset, (0,0))
rond=lambda x: 2*(round(x/2,-1))
length=1
x=20
y=20
go = 1    

class tail(Sprite):
    asset=RectangleAsset(20,20,line, purple)
    def __init__(self, position):
        super().__init__(tail.asset, position)
class ntail(Sprite):
    asset=RectangleAsset(20,20,line, black)
    def __init__(self, position):
        super().__init__(ntail.asset, position)

tail((x,y))

def leftKey(event):
    global up
    up=0
def rightKey(event):
    global up
    up=1    
def upKey(event):
    global up
    up=2
def downKey(event):
    global up
    up=3
def spaceKey(event):
    go=0

if (x+20)>SCREEN_WIDTH or (y+20)>SCREEN_HEIGHT or x<0 or y<0:
    go=0
    print("You lose.")

if go==1:
    if up==1:
        ntail(x,y)
        x=x+20
        tail(x,y)
        


dot=[(20*randint(0,40), 20*randint(0,30))]
for (x,y) in dot:
    tail((x,y))
            
myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
myapp.listenKeyEvent('keydown', 'j', leftKey)
myapp.listenKeyEvent('keydown', 'i', upKey)
myapp.listenKeyEvent('keydown', 'k', downKey)
myapp.listenKeyEvent('keydown', 'l', rightKey)
myapp.listenKeyEvent('keydown', 'space', spaceKey)