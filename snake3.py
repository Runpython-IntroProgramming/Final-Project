from ggame import App, RectangleAsset, ImageAsset, SoundAsset, CircleAsset
from ggame import LineStyle, Color, Sprite, Sound
from random import randint

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

blue=Color(0x87cefa, 1)
purple=Color(0x7b68ee, 1)
line=LineStyle(0,blue)
black = Color(0, 1)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, line, black)
bg = Sprite(bg_asset, (0,0))
x=20
y=20
z=3
snk=[(20,20)]
lose= False
go= False
dir=0

class tail(Sprite):
    asset=RectangleAsset(20,20,line, purple)
    def __init__(self, position):
        super().__init__(tail.asset, position)

class dots(Sprite):
    asset=RectangleAsset(20,20,line, blue)
    def __init__(self, position):
        super().__init__(dots.asset, position)

dot=[(20*randint(0,39), 20*randint(0,29))]
for (h,k) in dot:
    dt=[dots((h,k))]
snak=[tail((x,y))]    

def playagain(event):
    global dot, snk, x,y,z,go,dir,dt, snak, lose
    x=20
    y=20
    z=3
    snk=[(20,20)]
    lose = False
    dir=0
    for h in snak:
        h.destroy()
    for h in dt:
        h.destroy()
    dot=[(20*randint(0,39), 20*randint(0,29))]
    for (h,k) in dot:
        dt=[dots((h,k))]
    snak=[tail((x,y))]
    go=False

def leftKey(event):
    global dir, go
    if dir!=1 or len(snk)==1:
        dir=0
    go=True
    z=3
def rightKey(event):
    global dir, go
    if dir!=0 or len(snk)==1:
        dir=1
    go=True
    z=3
def downKey(event):
    global dir, go
    if dir!=3 or len(snk)==1:
        dir=2
    go=True
    z=3
def upKey(event):
    global dir, go
    if dir!=2 or len(snk)==1:
        dir=3
    go=True
    z=3
def spaceKey(event):
    global go
    if go:
        go=False
        
def step():
    global x, y, go, dir, z, dot, snk, snak, dt, lose
    if go and not lose:
        z=z+1
        if z==4:
            if dir==0:
                x=x-20
                for (h,k) in dot:
                    for (c,d) in snk:
                        if x==c and y==d:
                            print("you lose. Press r to play again.")
                            lose=True
                    if x==h and y==k:
                        snk.append((x,y))
                        snak.append(tail((x,y)))
                        dot[0]=(20*randint(0,39), 20*randint(0,29))
                        for (z,q) in dot:
                            dt[0].destroy()
                            dt[0]=(dots((z,q)))
                    elif (x+20)>SCREEN_WIDTH or (y+20)>SCREEN_HEIGHT or x<0 or y<0:
                        print("you lose. Press r to play again.")
                        lose=True
                    else:
                        snk.append((x,y))
                        snak.append(tail((x,y)))
                        snk.remove(snk[0])
                        snak[0].destroy()
                        snak.remove(snak[0])
            if dir ==1:
                x=x+20
                for (h,k) in dot:
                    for (c,d) in snk:
                        if x==c and y==d:
                            print("you lose. Press r to play again.")
                            lose=True
                    if x==h and y==k:
                        snk.append((x,y))
                        snak.append(tail((x,y)))
                        dot[0]=(20*randint(0,39), 20*randint(0,29))
                        for (z,q) in dot:
                            dt[0].destroy()
                            dt[0]=(dots((z,q)))
                    elif (x+20)>SCREEN_WIDTH or (y+20)>SCREEN_HEIGHT or x<0 or y<0:
                        print("you lose. Press r to play again.")
                        lose=True
                    else:
                        snk.append((x,y))
                        snak.append(tail((x,y)))
                        snk.remove(snk[0])
                        snak[0].destroy()
                        snak.remove(snak[0])
            if dir ==2:
                y=y+20
                for (h,k) in dot:
                    for (c,d) in snk:
                        if x==c and y==d:
                            print("you lose. Press r to play again.")
                            lose=True
                    if x==h and y==k:
                        snk.append((x,y))
                        snak.append(tail((x,y)))
                        dot[0]=(20*randint(0,39), 20*randint(0,29))
                        for (z,q) in dot:
                            dt[0].destroy()
                            dt[0]=(dots((z,q)))
                    elif (x+20)>SCREEN_WIDTH or (y+20)>SCREEN_HEIGHT or x<0 or y<0:
                        print("you lose. Press r to play again.")
                        lose=True
                    else:
                        snk.append((x,y))
                        snak.append(tail((x,y)))
                        snk.remove(snk[0])
                        snak[0].destroy()
                        snak.remove(snak[0])
            if dir ==3:
                y=y-20
                for (h,k) in dot:
                    for (c,d) in snk:
                        if x==c and y==d:
                            print("you lose. Press r to play again.")
                            lose=True
                    if x==h and y==k:
                        snk.append((x,y))
                        snak.append(tail((x,y)))
                        dot[0]=(20*randint(0,39), 20*randint(0,29))
                        for (z,q) in dot:
                            dt[0].destroy()
                            dt[0]=(dots((z,q)))
                    elif (x+20)>SCREEN_WIDTH or (y+20)>SCREEN_HEIGHT or x<0 or y<0:
                        print("you lose. Press r to play again.")
                        lose=True
                    else:
                        snk.append((x,y))
                        snak.append(tail((x,y)))
                        snk.remove(snk[0])
                        snak[0].destroy()
                        snak.remove(snak[0])
            z=0
        
myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run(step)
myapp.listenKeyEvent('keydown', 'left arrow', leftKey)
myapp.listenKeyEvent('keydown', 'up arrow', upKey)
myapp.listenKeyEvent('keydown', 'down arrow', downKey)
myapp.listenKeyEvent('keydown', 'right arrow', rightKey)
myapp.listenKeyEvent('keyup', 'space', spaceKey)
myapp.listenKeyEvent('keyup', 'r', playagain)
