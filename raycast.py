from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from math import sin, cos,tan, radians

mapw= 100
maph=100
scrw=640
scrh=480
SCREEN_WIDTH = scrw
SCREEN_HEIGHT = scrh

black = Color(0x000000, 1.0)
red = Color(0xff0000, 1.0)
white = Color(0xffffff, 1.0)

width=list(range(0,int((scrw/10))+1))
height = list(range(0,int((scrh/10))+1))

mwidth=list(range(0,int((mapw/10))+1))
mheight = list(range(0,int((maph/10))+1))
print(width)
print(height)
click = 0

walls={"0101":"0"}
for x in mwidth:
    for y in mheight:
        walls['0'+str(x)+'0'+str(y)]=0

thinline = LineStyle(1, black)
noline= LineStyle(0,black)
rsquare_asset =RectangleAsset(10,10, thinline, red)
wsquare_asset = RectangleAsset(10, 10, thinline, white)
nosquare_asset = RectangleAsset(10, 10, noline, white)

for x in width:
    for y in height:
        Sprite(nosquare_asset,(x*10, y*10))
        
for x in mwidth:
    for y in mheight:
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

Position={"x":"50","y":"50","dir":"0"}
change=1

def right(event):
    global change
    change=1
    if Position['dir']<360:
        Position['dir']=Position[x]+1
    else:
        Position['dir']=0

def left(event):
    global change
    change=1
    if Position['dir']>0:
        Position['dir']=Position[x]-1
    else:
        Position['dir']=359
        
def up(event):
    global change
    change=1
        Position['x']=Position['x']+sin(int(Position['x']))
        Position['y']=Position['y']+cos(int(Position['x']))
        
def down(event):
    global change
    change=1
        Position['x']=Position['x']-sin(int(Position['x']))
        Position['y']=Position['y']-cos(int(Position['x']))
    
def ray():
    global position
    global change
    if change==1:
        raydir=Position['dir']
        wall=0
        distance=0
        intilex=Position['x']-int(Position['x'])//1
        intiley=Position['y']-int(Position['y'])//1
        rayx=(Position['x']*10)//10) 
        rayy=(Position['y']*10)//10
        while wall==0:
            if walls['0'+str(round(rayx))+'0'+str(round(rayy))]==1:
                Sprite()
                raydir=raydir+10/distance
                wall=1
            else:
                distance=distance+1
                rayx=rayx+cos(radians(raydir))
                rayy=rayy+sin(radians(raydir))

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenMouseEvent('mouseup', mouseup)
myapp.listenMouseEvent('mousedown', mouseclick)
myapp.listenMouseEvent('mousemove', drag)
myapp.listenKeyEvent('keydown', 'right', right)
myapp.listenKeyEvent('keydown', 'left', left)
myapp.listenKeyEvent('keydown', 'up', up)
myapp.listenKeyEvent('keydown', 'down', down)

myapp = App()
myapp.run(ray)