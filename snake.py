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
go=1    

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
    global up, go
    up=0
    go=1
def rightKey(event):
    global up, go
    up=1   
    go=1
def upKey(event):
    global up, go
    up=2
    go=1
def downKey(event):
    global up, go
    up=3
    go=1
def spaceKey(event):
    global go
    go=0

while go==1:
    while (x+20)<=SCREEN_WIDTH and (y+20)<=SCREEN_HEIGHT and x>=0 and y>=0:
        if up==0:
            print("left")
            x=400000
        if up==1:
            print("right")
            x=400000
        if up==2:
            print("up")
            x=400000
        if up==3:
            print("down")
            x=400000

    
    if (x+20)>SCREEN_WIDTH or (y+20)>SCREEN_HEIGHT or x<0 or y<0:
        go=0
        print("You lose.")   

dot=[(20*randint(0,40), 20*randint(0,30))]
for (h,k) in dot:
    tail((h,k))

         


myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
myapp.listenKeyEvent('keydown', 'j', leftKey)
myapp.listenKeyEvent('keydown', 'i', upKey)
myapp.listenKeyEvent('keydown', 'k', downKey)
myapp.listenKeyEvent('keydown', 'l', rightKey)
myapp.listenKeyEvent('keydown', 'space', spaceKey)