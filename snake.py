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
snk=[(20,20)]


class tail(Sprite):
    asset=RectangleAsset(20,20,line, purple)
    def __init__(self, position):
        super().__init__(tail.asset, position)
class ntail(Sprite):
    asset=RectangleAsset(20,20,line, black)
    def __init__(self, position):
        super().__init__(ntail.asset, position)
class dots(Sprite):
    asset=RectangleAsset(20,20,line, blue)
    def __init__(self, position):
        super().__init__(dots.asset, position)

dot=[(20*randint(0,39), 20*randint(0,29))]
for (h,k) in dot:
    dots((h,k))
    
tail((x,y))

def leftKey(event):
    global x, y, snk, dot
    x=x-20
    for (h,k) in dot:
        if x==h and y==k:
            snk.append((x,y))
            tail((x,y))
            dot[0]=(20*randint(0,39), 20*randint(0,29))
            for (z,q) in dot:
                dots((z,q))
        elif (x+20)>SCREEN_WIDTH or (y+20)>SCREEN_HEIGHT or x<0 or y<0:
            print("you lose")
            go=0
            ntail(snk[0])
            quit()
        else:
            ntail(snk[0])
            tail((x,y))
            snk.append((x,y))
            snk.remove(snk[0])
def rightKey(event):
    global x, y, snk, dot
    x=x+20
    for (h,k) in dot:
        if x==h and y==k:
            snk.append((x,y))
            tail((x,y))
            dot[0]=(20*randint(0,39), 20*randint(0,29))
            for (z,q) in dot:
                dots((z,q))
        elif (x+20)>SCREEN_WIDTH or (y+20)>SCREEN_HEIGHT or x<0 or y<0:
            print("you lose")
            go=0
            ntail(snk[0])
            quit()
        else:
            ntail(snk[0])
            tail((x,y))
            snk.append((x,y))
            snk.remove(snk[0])

def upKey(event):
    global x, y, snk
    e=0
    y=y-20
    for (h,k) in dot:
        """for (c,d) in snk:
            if x==c and y==d:
                e=e+1
        if e==2:
            print("you lose")
            ntail(snk[0])
            quit()"""
        if x==h and y==k:
            snk.append((x,y))
            tail((x,y))
            dot[0]=(20*randint(0,39), 20*randint(0,29))
            for (z,q) in dot:
                dots((z,q))
        elif (x+20)>SCREEN_WIDTH or (y+20)>SCREEN_HEIGHT or x<0 or y<0:
            print("you lose")
            ntail(snk[0])
            quit()
        else:
            ntail(snk[0])
            tail((x,y))
            snk.append((x,y))
            snk.remove(snk[0])

def downKey(event):
    global x, y, snk
    y=y+20
    for (h,k) in dot:
        if x==h and y==k:
            snk.append((x,y))
            tail((x,y))
            dot[0]=(20*randint(0,39), 20*randint(0,29))
            for (z,q) in dot:
                dots((z,q))
        elif (x+20)>SCREEN_WIDTH or (y+20)>SCREEN_HEIGHT or x<0 or y<0:
            print("you lose")
            ntail(snk[0])
            quit()
        else:
            ntail(snk[0])
            tail((x,y))
            snk.append((x,y))
            snk.remove(snk[0])
    

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
myapp.listenKeyEvent('keydown', 'j', leftKey)
myapp.listenKeyEvent('keydown', 'i', upKey)
myapp.listenKeyEvent('keydown', 'k', downKey)
myapp.listenKeyEvent('keydown', 'l', rightKey)
#myapp.listenKeyEvent('keyup', 'space', spaceKey)