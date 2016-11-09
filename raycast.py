from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

mapw= 100
maph=100
scrw=640
scrh=480
SCREEN_WIDTH = scrw
SCREEN_HEIGHT = scrh

black = Color(0x000000, 1.0)
red = Color(0xff0000, 1.0)
white = Color(0xffffff, 1.0)

width=list(range(0,int((mapw/10))+1))
height = list(range(0,int((maph/10))+1))
print(width)
print(height)
click = 0

walls={"0101":"0"}
for x in width:
    for y in height:
        walls['0'+str(x)+'0'+str(y)]=0

thinline = LineStyle(1, black)
rsquare_asset =RectangleAsset(10,10, thinline, red)
wsquare_asset = RectangleAsset(10, 10, thinline, white)
for x in width:
    for y in height:
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

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenMouseEvent('mouseup', mouseup)
myapp.listenMouseEvent('mousedown', mouseclick)
myapp.listenMouseEvent('mousemove', drag)
myapp.listenKeyEvent('keydown', 'space', spacekey)

myapp = App()
myapp.run()