from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from math import sin, cos,tan, radians, atan2

mapw= 100
maph=100
scrw=1000
scrh=640
SCREEN_WIDTH = scrw
SCREEN_HEIGHT = scrh

black = Color(0x000000, 1.0)
red = Color(0xff0000, 1.0)
white = Color(0xffffff, 1.0)
b1 = Color(0x0000ff, 1.0)
b2 = Color(0x0000e5, 1.0)
b3 = Color(0x0000cc, 1.0)
b4 = Color(0x0000b2, 1.0)
b5 = Color(0x000099, 1.0)
b6 = Color(0x00007f, 1.0)
b7 = Color(0x000066, 1.0)
b8 = Color(0x00004c, 1.0)
b9 = Color(0x000033, 1.0)
b10 = Color(0x000019, 1.0)
b11 = Color(0x000000, 1.0)

width=list(range(0,int((scrw/10))+1))
height = list(range(0,int((scrh/10))+1))

mwidth=list(range(0,int((mapw/10))+1))
mheight = list(range(0,int((maph/10))+1))
print(mwidth)
print(mheight)
click = 0

go=0
screenside=0

walls={"0101":"0"}
for x in mwidth:
    for y in mheight:
        if x==0 or y==0 or x==mapw//10 or y==maph//10:
            walls['0'+str(x)+'0'+str(y)]=1
        else:
            walls['0'+str(x)+'0'+str(y)]=0

thinline = LineStyle(1, black)
noline= LineStyle(0,black)
rsquare_asset =RectangleAsset(10,10, thinline, red)
wsquare_asset = RectangleAsset(10, 10, thinline, white)
nosquare_asset = RectangleAsset(10, 10, noline, white)

for x in mwidth:
    for y in mheight:
        if x==0 or y==0 or x==mapw//10 or y==maph//10:
            Sprite(rsquare_asset,(x*10, y*10))
        else:
            Sprite(wsquare_asset,(x*10, y*10))

def mouseclick(event):
    global click
    click = 1
    pixelpositionx = ((event.x)//10)*10
    pixelpositiony = ((event.y)//10)*10
    if walls['0'+str(round(pixelpositionx/10))+'0'+str(round(pixelpositiony/10))]==0:
        Sprite(rsquare_asset, (pixelpositionx, pixelpositiony))
        walls['0'+str(round(pixelpositionx/10))+'0'+str(round(pixelpositiony/10))]=1
    else:
        Sprite(wsquare_asset, (pixelpositionx, pixelpositiony))
        walls['0'+str(round(pixelpositionx/10))+'0'+str(round(pixelpositiony/10))]=0
        
def mouseup(event):        
    global click
    click = 0
    
def drag(event):
    global click
    if click==1:
        pixelpositionx = ((event.x)//10)*10
        pixelpositiony = ((event.y)//10)*10
        if walls['0'+str(round(pixelpositionx/10))+'0'+str(round(pixelpositiony/10))]==0:
            Sprite(rsquare_asset, (pixelpositionx, pixelpositiony))
            walls['0'+str(round(pixelpositionx/10))+'0'+str(round(pixelpositiony/10))]=1
        else:
            Sprite(wsquare_asset, (pixelpositionx, pixelpositiony))
            walls['0'+str(round(pixelpositionx/10))+'0'+str(round(pixelpositiony/10))]=0

Position={"x":5,"y":5,"dir":90}
change=1
first=1

def right(event):
    global change
    global first
    change=1
    first=1
    if Position['dir']<360:
        Position['dir']=Position['dir']+1
    else:
        Position['dir']=0

def left(event):
    global first
    global change
    change=1
    first=1
    if Position['dir']>0:
        Position['dir']=Position['dir']-1
    else:
        Position['dir']=359
        
def up(event):
    global change
    global first
    change=1
    first=1
    sqdir=(int(Position['dir'])//90)*90
    if sqdir==0:
        Position['x']=int(Position['x'])+1
    if sqdir==90:
        Position['y']=int(Position['y'])+1
    if sqdir==180:
        Position['x']=int(Position['x'])-1
    if sqdir==270:
        Position['y']=int(Position['y'])-1
        
def down(event):
    global change
    global first
    change=1
    first=1
    sqdir=(int(Position['dir'])//90)
    if sqdir==0:
        Position['x']=Position['x']-1
    if sqdir==1:
        Position['y']=Position['y']-1
    if sqdir==2:
        Position['x']=Position['x']+1
    if sqdir==3:
        Position['y']=Position['y']+1
def space(event):
    global go
    if go==0:
        go=1
    else:
        go=0
wall=True
raydir=0
inpov=0
def ray():
    global wall
    global inpov
    global raydir
    global first
    global scrh
    global walls
    global go
    global position
    global change
    global screenside
    if change==1 and go==1:
        clear=RectangleAsset(1000,640, noline, white)
        if first==1:
            Sprite(clear,(110,0))
            raydir=int(Position['dir'])-45
            inpov=0
            first=0
            oldrayx=0
            oldrayy=0
        print('ray has started')
        wall=False
        distance=0
        intilex=int(Position['x'])-int(Position['x'])//1
        intiley=int(Position['y'])-int(Position['y'])//1
        rayx=(int(Position['x'])*10)//10
        rayy=(int(Position['y'])*10)//10
        while wall==False:
            print('0'+str(round(rayx))+'0'+str(round(rayy)))
            print(walls['0'+str(round(rayx))+'0'+str(round(rayy))])
            if walls['0'+str(round(rayx))+'0'+str(round(rayy))]==1:
                print("player position:",(int(Position['x'])*10)//10,(int(Position['y'])*10)//10)
                print("x wall:",round(rayx))
                print("y wall:",round(rayy))
                inpov=abs(raydir-int(Position['dir']))
                xdif=(int(Position['x'])-round(rayx))
                ydif=(int(Position['y'])-round(rayy))**2
                distance1=(abs(xdif)**2+abs(ydif))**(1/2)
                print(inpov)
                sidedistance=abs(45-screenside)
                if round(rayx)!=oldrayx or round(rayy)!=oldrayy:
                    distance=distance1*sin(radians(90-(atan2(xdif,ydif))))
                    oldrayx=round(rayx)
                    oldrayy=round(rayy)
                print("distance:", distance)
                wallbox=RectangleAsset(((10/float(distance))),10*(200/(float(distance))), thinline, b5)
                Sprite(wallbox,(screenside+110,(scrh/2)-(10*(200/(float(distance))))/2))
                raydir=raydir+1/distance
                screenside=screenside+10/distance
                wall=True
                if inpov>=46:
                    change=0
                    screenside=0
                    print(change)
            else:
                distance=distance+1
                rayx=rayx+cos(radians(raydir))
                rayy=rayy+sin(radians(raydir))

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenMouseEvent('mouseup', mouseup)
myapp.listenMouseEvent('mousedown', mouseclick)
myapp.listenMouseEvent('mousemove', drag)
myapp.listenKeyEvent('keydown', 'd', right)
myapp.listenKeyEvent('keydown', 'a', left)
myapp.listenKeyEvent('keydown', 'w', up)
myapp.listenKeyEvent('keydown', 's', down)
myapp.listenKeyEvent('keydown', 'space', space)

myapp = App()
myapp.run(ray)